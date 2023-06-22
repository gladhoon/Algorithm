from collections import deque
move = [[-1,0], [1,0], [0,-1], [0,1]]
def bfs(x, y):
    visited[x][y] = True
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                maze[nx][ny] = maze[x][y] + 1
                q.append([nx, ny])
    print(visited)
    return maze[n-1][m-1]

n, m = map(int, input().split())
maze = []
visited = [[False]*m for _ in range(n)]
for _ in range(n):
    maze.append(list(map(int, input())))
    
print(bfs(0,0))
