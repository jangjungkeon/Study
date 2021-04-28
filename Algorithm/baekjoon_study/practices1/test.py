import sys


def dp_func(N, A):
    dp_as = [1 for _ in range(N)]
    dp_ds = [1 for _ in range(N)]
    # ascend
    for i in range(1, N):
        for j in range(i):
            if A[i] > A[j] and dp_as[j]+1 > dp_as[i]:
                dp_as[i] = dp_as[j]+1

    for i in range(1, N):
        for j in range(i):
            if A[i] < A[j] and dp_ds[j]+1 > dp_ds[i]:
                dp_ds[i] = dp_ds[j]+1

    return


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    A = list(map(int, sys.stdin.readline().split()))
    dp_func(N, A)
