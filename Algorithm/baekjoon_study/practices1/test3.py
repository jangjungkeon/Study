n = 4
start = 1
end = 4
roads = [[1, 2, 1], [3, 2, 1], [2, 4, 1]]
e = len(roads)
traps = [2, 3]

grape = [[] for _ in range(n+1)]
for i in roads:
    grape[i[0]].append([i[1], i[2]])

current = 2
print(grape)
if current in traps:
    # 2에서 나오는 것
    tmp



