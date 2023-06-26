import sys
input = sys.stdin.readline

n = int(input())
arr = [[0]*(n+1)] + [[0] + list(map(int, input().split())) for _ in range(n)]

dp = [[[0] * 10 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,10):
            if k == arr[i][j]:
                dp[i][j][k] += 1
            dp[i][j][k] += dp[i-1][j][k] + dp[i][j-1][k] - dp[i-1][j-1][k]

q = int(input())
for _ in range(q):
    x1, y1, x2, y2 = map(int, input().split())
    result = 0
    for k in range(1,10):
        if dp[x2][y2][k] - dp[x2][y1-1][k] - dp[x1-1][y2][k] + dp[x1-1][y1-1][k]:
            result += 1
    print(result)