import sys


def dp_func(N, A):
    dp = [1 for _ in range(N)]

    for i in range(1, N):
        for j in range(i):
            if A[i] > A[j] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1

    print(max(dp))



    return


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    A = list(map(int, sys.stdin.readline().split()))
    dp_func(N, A)
