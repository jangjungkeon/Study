import sys
import heapq


def daextra():
    # dp[i] : start 에서 i 까지 최단거리
    dp = [INF for _ in range(V+1)]
    dp[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))      # (경로, 인덱스)

    while heap:
        # 현재 테이블에서 가장 가까운 정점을 선택
        weight, current = heapq.heappop(heap)
        # print("current : ", current)

        # 불필요한 튜플은 제거
        if dp[current] < weight:
            continue

        # 정점에서 갈 수 있는 정점을 조사
        for w, next_node in grape[current]:
            next_wei = w + weight
            if next_wei < dp[next_node]:
                dp[next_node] = next_wei
                heapq.heappush(heap, (next_wei, next_node))
    # 출력
    for k in range(1, V+1):
        print("INF" if dp[k] == INF else dp[k])

    return


if __name__ == "__main__":
    V, E = map(int, sys.stdin.readline().split())
    start = int(sys.stdin.readline().strip())
    INF = 100000000
    grape = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v, w = map(int, sys.stdin.readline().split())
        grape[u].append((w, v))
    daextra()
