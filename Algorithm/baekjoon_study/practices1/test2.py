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
    tmp_out = []
    tmp_list = []
    if grape[current]:
        tmp_out = grape[current]
    for i in tmp_out:
        grape[i[0]].append([current, i[1]])
        grape[current].remove(i)
        tmp_list.append(i[0])


    # 2에서 들어오는 것
    for i in range(1, n+1):
        if i == current:
            continue
        if i in tmp_list:
            continue
        for j in grape[i]:
            if j[0] == current:
                grape[current].append([i, j[1]])
                grape[i].remove([current, j[1]])








