import sys


def dp_func():
    M = [[0 for _ in range(N)] for _ in range(N)]
    for d in range(1, N):
        for i in range(N-d):
            j = i + d
            M[i][j] = min([M[i][k] + M[k+1][j] + D[i-1]*D[k]*D[j] for k in range(i, j)])

    return print(M[0][N-1])


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    Matrix = []
    D = []
    for _ in range(N):
        r, c = map(int, sys.stdin.readline().split())
        Matrix.append([r, c])
        D.append(r)
    D.append(Matrix[-1][-1])
    dp_func()
