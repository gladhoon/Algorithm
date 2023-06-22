n, k = map(int, input().split())
coin = []
cnt = 0

for i in range(n):
    a = int(input())
    coin.append(a)

for i in range(n-1,-1,-1):
    if k >= coin[i]:
        k -= coin[i]
        cnt += 1
        i += 1

print(cnt)