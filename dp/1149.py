n = int(input())
graph = []
dp = [[0 for _ in range(3)] for _ in range(n)]
for _ in range(n):
    r, g, b = map(int ,input().split())
    graph.append([r, g, b])

dp[0] = graph[0]

for i in range(1,n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + graph[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + graph[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + graph[i][2]

print(min(dp[n-1]))