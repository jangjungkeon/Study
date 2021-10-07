import collections

n = 8
k = 2
remember = collections.deque()
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
origin = [i for i in range(n)]
result = [i for i in range(n)]
answer = ["X" for _ in range(n)]
# 항상 현재 위치를 기억해두어야할듯?
for i in cmd:
    cmd_spec = i.split()
    if cmd_spec[0] == "D":
        num = cmd_spec[1]
        k += int(num)
    elif cmd_spec[0] == "U":
        num = cmd_spec[1]
        k -= int(num)
    elif cmd_spec[0] == "C":
        # (현재위치, 이름)
        remember.append((k, result[k]))
        del result[k]
        # 마지막행이라면
        if len(result) == k:
            k -= 1

    elif cmd_spec[0] == "Z":
        index, name = remember.pop()
        result.insert(index, name)
        if index <= k:
            k += 1

for i in result:
    answer[i] = "O"

print("".join(answer))
