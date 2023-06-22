from collections import deque
def bfs(x):
    count = 0
    q = deque([x])
    visited[x] = True
    while q:
        node = q.popleft()
        for i in arr[node]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                count += 1

    return count

count = 0
def dfs(x):
    visited[x] = True
    for i in arr[x]:
        if not visited[i]:
            dfs(i)

v = int(input())    # 노드
e = int(input())    # 간선 개수
arr = [[] for _ in range(v+1)]
visited = [False] * (v+1)
for _ in range(e):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

print(bfs(1))
dfs(1)
print(sum(visited)-1)