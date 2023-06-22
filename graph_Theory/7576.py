from collections import deque
import sys
input = sys.stdin.readline
m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
q = deque()
ans = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append([i,j])

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1
                q.append([nx,ny])

for i in arr:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    ans = max(ans, max(i))

print(ans-1)