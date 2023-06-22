s = input().upper()
alpha = list(set(s))
arr = []
cnt = 0

for i in alpha:
    cnt = s.count(i)
    arr.append(cnt)

if arr.count(max(arr)) > 1:
    print('?')
else:
    print(alpha[arr.index(max(arr))])