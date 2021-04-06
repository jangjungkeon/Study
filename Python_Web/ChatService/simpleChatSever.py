# 멀티 채팅 서버, 멀티 쓰레드
import socket, threading

# 소켓 인스턴스 생성 socket.socket(소캣 family, 소캣 type)
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = '127.0.0.1'
PORT = 5000
ss.bind((HOST, PORT))
ss.listen(5)  # 보류 중인 연결 큐의 최대 길이 = 5
print('채팅 서비스 시작. ')
users = []


# 쓰레드로 돌릴 함수 인스턴스
def chatUser(conn):
    name = conn.recv(1024)
    data = name.decode('utf-8') + '님 입장 ~'
    print(data)

    try:
        # 기존 사용자에게 입장한 사용자를 알리기
        for p in users:
            p.send(data.encode('utf-8'))

        # 채팅 하기
        while True:
            msg = conn.recv(1024)
            data = name.decode('utf-8') + '님 메세지: ' + msg.decode('utf-8')
            print('수신 : ', data)
            for p in users:
                p.send(data.encode('utf-8'))
    except:
        users.remove(conn)
        data = name.decode('utf-8') + '님 퇴장'
        print(data)
        if users:
            for p in users:
                p.send(data.encode('utf-8'))
        else:
            print('exit')


while True:
    conn, addr = ss.accept()
    users.append(conn)
    th = threading.Thread(target=chatUser, args=(conn,))
    th.start()
