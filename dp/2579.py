n = int(input())
arr = []
dp = [0]
for _ in range(n):
    arr.append(int(input()))

cnt = 1
for i in range(n-2):
    if arr[i]+arr[i+1] > arr[i+2] and cnt != 2:
        dp.append(arr[i] + arr[i+1] + dp[i-1])
        cnt += 1
        i += 2
    else:
        dp.append(arr[i+1]+dp[len(dp)-1])
        cnt = 1
print(dp)