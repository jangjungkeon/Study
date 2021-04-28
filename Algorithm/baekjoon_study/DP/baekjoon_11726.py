import sys


def dp_func(N):
    if N == 1:
        return print(1)
    dp = [0 for _ in range(N+1)]
    dp[1] = 1
    dp[2] = 2

    # 노가다로 해보고 알았음. 점화식의 규칙만 찾으면 된다. 자연의 원리 까지 끌여들여 깊게 생각할 필요는 없다.
    # 문제서 요구하는 규칙을 찾아내기만 하면된다.
    for i in range(3, N+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 10007

    return print(dp[N])


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    dp_func(N)
