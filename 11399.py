n = int(input())
arr = list(map(int, input().split()))
ans = 0
arr.sort()
for i in range(1,n):
    arr[i] = arr[i] + arr[i-1]
    ans += arr[i]

print(ans+arr[0])