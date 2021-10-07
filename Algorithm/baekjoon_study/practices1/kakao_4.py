## 문제는 못품.
## 15분정도만 더 있었으면 풀었을텐데 아쉽다.

import heapq
import sys

n = 3
start = 1
end = 3
roads = [[1, 2, 2], [3, 2, 3]]
e = len(roads)
traps = [2]

grape = [[] for _ in range(n + 1)]
for i in range(e):
    grape[i[0]].append([i[1], i[2]])

INF = sys.maxsize
dp = [INF for _ in range(n + 1)]
dp[start] = 0
heap = [(0, start)]

while heap:
    # 현재 테이블에서 가장 가까운 정점을 선택
    weight, current = heapq.heappop(heap)

    # 함정에 위치한다면 grape 변경
    if current in traps:
        # 2에서 나오는 것
        tmp_out = []
        tmp_list = []
        if grape[current]:
            tmp_out = grape[current]
        for i in tmp_out:
            grape[i[0]].append([current, i[1]])
            grape[current].remove(i)
            tmp_list.append(i[0])

        # 2에서 들어오는 것
        for i in range(1, n + 1):
            if i == current:
                continue
            if i in tmp_list:
                continue
            for j in grape[i]:
                if j[0] == current:
                    grape[current].append([i, j[1]])
                    grape[i].remove([current, j[1]])

    # 불필요한 튜플은 제거
    if dp[current] < weight:
        continue

    # 정점에서 갈 수 있는 정점을 조사
    for w, next_node in grape[current]:
        if w + weight < dp[next_node]:
            dp[next_node] = w + weight
            heapq.heappush(heap, (w + weight, next_node))

print(dp[end])

