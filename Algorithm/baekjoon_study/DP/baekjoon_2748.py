import sys


def func(N):
    dp = [0 for _ in range(91)]
    dp[1] = 1
    for i in range(2, N+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[N]


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    print(func(N))
