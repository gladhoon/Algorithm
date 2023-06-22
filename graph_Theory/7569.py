import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
q = deque()
ans = 0

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1:
                q.append([i, j, k])

while q:
    x, y, z = q.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]

        if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and arr[nx][ny][nz] == 0:
            q.append([nx, ny, nz])
            arr[nx][ny][nz] = arr[x][y][z] + 1

for i in arr:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        ans = max(ans, max(j))

print(ans-1)