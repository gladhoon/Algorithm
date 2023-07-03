arr = input()
n = len(arr)
value = [0] * (n+1)
count = [0] * (n+1)
dic = {}
answer = -1

for i in range(n):
    t = 0
    if arr[i] == 'S':
        t = 2
    elif arr[i] == 'K':
        t = -1
    value[i+1] = value[i] + t
    if t == 0:
        count[i+1] = count[i]
    else:
        count[i+1] = count[i] + 1

for i in range(n+1):
    if value[i] not in dic:
        dic[value[i]] = i
    else:
        index = dic[value[i]]
        if count[index] == count[i]:
            continue
        answer = max(answer, i-index)

print(answer)