n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = 0
for i in range(m):
    if (i+1)%k == 0:
        ans += arr[-2]
    else:
        ans += arr[-1]

print(ans)