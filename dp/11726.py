dp = [0, 1, 2]
def func(n):
    if n >= len(dp):
        for i in range(len(dp), n+1):
            dp.append((dp[i-1] + dp[i-2])%10007)
    print(dp[n])

t = int(input())
func(t)