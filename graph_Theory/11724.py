import sys
from collections import deque
input = sys.stdin.readline
def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = True
    while q:
        x = q.popleft()
        if 1<=x<=n:
            for k in arr[x]:
                if not visited[k]:
                    visited[k] = True
                    q.append(k)
    return

n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

answer = 0
for i in range(1,n+1):
    if not visited[i]:
        bfs(i)
        answer += 1

print(answer)