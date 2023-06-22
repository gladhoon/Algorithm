from collections import deque

def dfs(start):
    visited_dfs[start] = True
    print(start, end= ' ')
    for i in range(1, n+1):
        if not visited_dfs[i] and arr[start][i]:
            dfs(i)

def bfs(start):
    visited_bfs[start] = True
    q = deque()
    q.append(start)
    while q:
        point = q.popleft()
        print(point, end=' ')
        for i in range(1,n+1):
            if not visited_bfs[i] and arr[point][i]:
                q.append(i)
                visited_bfs[i] = True


n, m, v = map(int, input().split())
arr = [[False] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a][b] = True
    arr[b][a] = True

visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)

dfs(v)
print()
bfs(v)