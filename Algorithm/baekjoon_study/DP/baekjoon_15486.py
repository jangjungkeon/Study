import sys


def dp_func():
    dp = [0 for _ in range(N + 1)]
    for i in range(N):
        if T[i] <= N - i:       # i 번째에 상담이 가능한 경우.
            dp[i + T[i]] = max(dp[i + T[i]], dp[i] + P[i])      # 전에 한 것과 새로한 것을 비교

        dp[i + 1] = max(dp[i + 1], dp[i])   # 일거리가 없더라도 전날 최대수익만큼이 오늘 수익이므로. 즉 어제 10 벌고 오늘 0 버는건 말이 안됨.

    return print(dp[N])


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    T, P = [], []

    for i in range(N):
        temp = list(map(int, sys.stdin.readline().split()))
        T.append(temp[0])
        P.append(temp[1])

    dp_func()
