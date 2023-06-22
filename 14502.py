import copy
from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque()
    copy_graph = copy.deepcopy(graph)
    for i in range(n):
        for j in range(m):
            if copy_graph[i][j] == 2:
                q.append([i,j])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if copy_graph[nx][ny] == 0:
                copy_graph[nx][ny] = 2
                q.append([nx,ny])
    global answer
    cnt = 0
    for i in range(n):
        cnt += copy_graph[i].count(0)

    answer = max(answer,cnt)

def wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                wall(cnt+1)
                graph[i][j] = 0

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

answer = 0
wall(0)
print(answer)