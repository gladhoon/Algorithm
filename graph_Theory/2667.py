from collections import deque
def bfs(x, y):
    count = 1
    arr[x][y] = 0
    d = [[-1,0], [1,0], [0,-1], [0,1]]
    q = deque()
    q.append([x,y])
    visited[x][y] = True
    while q:
        a, b = q.popleft()
        for x, y in d:
            nx = a + x
            ny = b + y
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if arr[nx][ny] > 0:
                    visited[nx][ny] = True
                    arr[nx][ny] = 0
                    q.append([nx, ny])
                    count += 1
    return count

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input())))

visited = [[False]*n for _ in range(n)]
ans = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            ans.append(bfs(i,j))
ans.sort()
print(len(ans))
for i in range(len(ans)):
    print(ans[i])