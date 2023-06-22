import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [-1,1,0,0]
def dfs(x,y):
    color = graph[x][y]
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n and graph[nx][ny] == color and visited[nx][ny] != True:
            visited[nx][ny] = True
            dfs(nx,ny)

cnt1, cnt2 = 0, 0
n = int(input())
graph = []
visited = [[False for _ in range(n)] for _ in range(n)]
for _ in range(n):
    graph.append(list(input().rstrip()))

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i,j)
            cnt1 += 1

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

visited = [[False for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i,j)
            cnt2 += 1

print(cnt1, cnt2)