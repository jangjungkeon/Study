import sys
sys.setrecursionlimit(10000)


def dp_func(a, b):
    if a == 0 and b == 0:
        return 1
    if dp[a][b] == -1:
        dp[a][b] = 0
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < M and 0 <= y < N and board[a][b] < board[x][y]:
                dp[a][b] += dp_func(x, y)
    return dp[a][b]


if __name__ == '__main__':
    M, N = map(int, sys.stdin.readline().split())
    board = []
    for _ in range(M):
        board.append(list(map(int, sys.stdin.readline().split())))
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    dp = [[-1 for _ in range(N)] for _ in range(M)]
    print(dp_func(M-1, N-1))
