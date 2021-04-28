import sys


def dp_func(N, A):
    dp = [1 for _ in range(N)]

    for i in range(1, N):
        tmp = []
        for j in range(i):
            if A[i] > A[j]:
                tmp.append(dp[j])
        if not tmp:
            continue
        else:
            dp[i] += max(tmp)

    return print(max(dp))


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    A = list(map(int, sys.stdin.readline().split()))
    dp_func(N, A)
