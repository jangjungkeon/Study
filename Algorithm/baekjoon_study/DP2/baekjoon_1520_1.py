# 시간초과
import sys
import collections


def dp_func():
    q = collections.deque()
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q.append([0, 0])
    cont = 0

    while q:
        a, b = q.popleft()
        if a == M-1 and b == N-1:
            cont += 1
            continue
        for k in range(4):
            x = a + dx[k]
            y = b + dy[k]
            if 0 <= x < M and 0 <= y < N and board[a][b] > board[x][y]:
                q.append([x, y])

    return print(cont)


if __name__ == '__main__':
    M, N = map(int, sys.stdin.readline().split())
    board = []
    for _ in range(M):
        board.append(list(map(int, sys.stdin.readline().split())))
    dp_func()

