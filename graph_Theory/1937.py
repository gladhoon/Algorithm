import sys
sys.setrecursionlimit(1000000)

def dfs(x, y):
    if arr[x][y]: return arr[x][y]
    arr[x][y] = 1
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < n and panda[x][y] < panda[nx][ny]:
            arr[x][y] = max(arr[x][y], dfs(nx, ny) + 1)
    return arr[x][y]

n = int(input())
panda = []
result = 0
for i in range(n):
    panda.append(list(map(int, sys.stdin.readline().split())))

dx = [0, 0, -1, 1]          # 상하좌우
dy = [1, -1, 0, 0]
arr = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        result = max(result, dfs(i, j))

print(result)