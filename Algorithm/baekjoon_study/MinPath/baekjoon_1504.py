import sys
import heapq


def min_path(start, end):
    # dp[i] : start 에서 i 까지 최단거리
    dp = [INF for _ in range(N + 1)]
    dp[start] = 0
    heap = [(0, start)]     # (경로, 인덱스)


    while heap:
        # 현재 테이블에서 가장 가까운 정점을 선택
        weight, current = heapq.heappop(heap)
        # print("current : ", current)

        # 불필요한 튜플은 제거
        if dp[current] < weight:
            continue

        # 정점에서 갈 수 있는 정점을 조사
        for w, next_node in grape[current]:
            if w + weight < dp[next_node]:
                dp[next_node] = w + weight
                heapq.heappush(heap, (w + weight, next_node))

    return dp[end]


if __name__ == "__main__":
    N, E = map(int, sys.stdin.readline().split())
    grape = [[] for _ in range(N+1)]
    INF = sys.maxsize
    for _ in range(E):
        a, b, c = map(int, sys.stdin.readline().split())
        grape[a].append((c, b))
        grape[b].append((c, a))
    print(grape)
    v1, v2 = map(int, sys.stdin.readline().split())
    result = min(min_path(1, v1) + min_path(v1, v2) + min_path(v2, N), min_path(1, v2) + min_path(v2, v1) + min_path(v1, N))
    print(result if result < INF else -1)


