n, m = map(int, input().split())
arr = list(map(int, input().split()))
t = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            total = arr[i] + arr[j] + arr[k]
            if t < total <= m:
                t = total
print(t)