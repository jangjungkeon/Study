import sys


def dp_func():
    c1_len = len(C1)
    c2_len = len(C2)
    # dp[i][j] : (c1의 i번째, c2의 j번째) 까지의 가장 긴 문자열길이
    dp = [[0 for _ in range(c2_len)] for _ in range(c1_len)]

    for i in range(1, c1_len):
        for j in range(1, c2_len):
            if C1[i] == C2[j]:          # 문자열이 같으면 전에 최대 길이(dp[i-1][j-1])에서 1추가
                dp[i][j] = dp[i-1][j-1] + 1
            else:                       # 문자열 길이가 다르면 dp[i-1][j], dp[i][j-1] 중 긴 것으로
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return print(dp[c1_len-1][c2_len-1])


if __name__ == "__main__":
    C1 = [0] + list(sys.stdin.readline().strip())
    C2 = [0] + list(sys.stdin.readline().strip())
    dp_func()
