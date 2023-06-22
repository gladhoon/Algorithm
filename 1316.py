n = int(input())
cnt = 0
for test_case in range(n):
    arr = set()
    word = input()

    if len(word) == 1:
        continue

    arr.add(word[0])
    for i in range(1,len(word)):
        alpha = word[i]
        if alpha != word[i-1] and alpha in arr:
            cnt += 1
            break
        arr.add(alpha)

print(n-cnt)