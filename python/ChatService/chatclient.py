# 멀티 채팅 클라이언트(simple ver)

import socket, sys, threading


# 클라이언트용 쓰레드
def Handle(socket):
    while True:
        data = socket.recv(1024)
        if not data:
            continue
        print(data.decode('utf-8'))


# 파이썬의 표준 출력은 버퍼링이 되므로 flush를 해주는 것이 좋다.
sys.stdout.flush()


# 소켓 인스턴스 생성 socket.socket(소캣 family, 소캣 type)
cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = '127.0.0.1'
PORT = 5000
cs.connect((HOST, PORT))         # ip : 127.0.0.1, port : 5000으로 바인딩
name = input('채팅 아이디 입력 : ')
cs.send(name.encode('utf-8'))

# 쓰레드 인스턴스 생성, args는 tuple로 써줘야함.
th = threading.Thread(target=Handle, args=(cs, ))
th.start()

while True:
    msg = input()
    sys.stdout.flush()
    if not msg:
        continue
    cs.send(msg.encode('utf-8'))

cs.close()
