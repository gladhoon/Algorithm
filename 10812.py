n, m = map(int, input().split())
arr = [_ for _ in range(1,n+1)]

for x in range(m):
    i, j, k = map(int, input().split())
    for y in range(k-i):
        arr.insert(j, arr[i-1])
        del arr[i-1]

print(*arr)