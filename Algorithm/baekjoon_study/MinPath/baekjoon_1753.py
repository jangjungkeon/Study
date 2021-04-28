import sys
from collections import deque


def min_path(i):
    if i == k:
        return 0
    # k ~ i 까지 최단거리
    w = 0
    q = deque()
    while q:
        pass


    return


if __name__ == "__main__":
    v, e = map(int, sys.stdin.readline().split())
    k = int(sys.stdin.readline().strip())
    g = []
    for _ in range(e):
        g.append(list(map(int, sys.stdin.readline().split())))
    for i in range(1, v+1):
        print(min_path(i))


















