import sys


def dp_func(N):
    dp = [0, 1, 2, 4]

    for i in range(4, N+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    return dp[N]


'''
정수 n을 1,2,3 으로 나타낼 수 있는 방법의 수 순서도 고려한다. 
dp[n] = dp[n-1] + dp[n-2] + dp[n-3] + 3
dp[4] = dp[3] + dp[2] + dp[1]
dp[4] = (4) + (2) + (1)
1 2 3 3 
'''

if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        print(dp_func(int(sys.stdin.readline().strip())))