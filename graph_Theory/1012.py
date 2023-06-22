from collections import deque

def bfs(x, y):
    d = [[-1,0], [1,0], [0,-1], [0,1]]
    q = deque()
    q.append([x,y])
    visited[x][y] = True
    graph[x][y] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if (0 > nx or nx >= n) or (0 > ny or ny >= m) or visited[nx][ny]:
                continue
            if graph[nx][ny]==1:
                visited[nx][ny] = True
                graph[nx][ny] = 0
                q.append([nx,ny])
    return


T = int(input())
for _ in range(1, T+1):
    answer = 0
    m, n, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    for i in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(i,j)
                answer += 1
    print(answer)