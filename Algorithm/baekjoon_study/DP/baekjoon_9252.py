import sys


def dp_func():
    c1_len = len(C1)
    c2_len = len(C2)
    # dp[i][j] : (c1의 i번째, c2의 j번째) 까지의 가장 긴 문자열
    dp = [["" for _ in range(c2_len)] for _ in range(c1_len)]

    for i in range(1, c1_len):
        for j in range(1, c2_len):
            if C1[i] == C2[j]:  # 문자가 같으면 바로전 이전에 가장 긴 문자열에 추가
                dp[i][j] = dp[i-1][j-1] + C1[i]
            else:           # dp[i-1][j] 와 dp[i][j-1] 중 길이가 긴 것으로 설정
                dp[i][j] = dp[i-1][j] if len(dp[i-1][j]) > len(dp[i][j-1]) else dp[i][j-1]

    print(len(dp[c1_len-1][c2_len-1]))
    if len(dp[c1_len - 1][c2_len - 1]) != 0:
        print(dp[c1_len-1][c2_len-1])
    return


if __name__ == "__main__":
    C1 = ['0'] + list(sys.stdin.readline().strip())
    C2 = ['0'] + list(sys.stdin.readline().strip())
    dp_func()
