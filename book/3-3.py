n, m = map(int, input().split())

ans = 0
for _ in range(n):
    arr = list(map(int, input().split()))
    value = min(arr)
    ans = max(ans, value)

print(ans)