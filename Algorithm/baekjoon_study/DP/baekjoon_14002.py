import sys


def dp_func(N, A):
    dp = [1 for _ in range(N)]
    array = [[a] for a in A]

    # dp 값과 가장 긴 수열 찾기
    for i in range(1, N):
        for j in range(i):
            if A[i] > A[j]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    array[i] = array[j] + [A[i]]

    # dp 에서 최댓값 찾기
    result = 0
    flag = 0
    for i in range(N):
        if result < dp[i]:
            result = dp[i]
            flag = i
    print(result)
    print(*array[flag])
    return


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    A = list(map(int, sys.stdin.readline().split()))
    dp_func(N, A)
