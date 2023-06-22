from collections import deque
def bfs(x):
    dx = [-1, 1, 2]
    q = deque()
    q.append(x)
    arr[x] = 0
    while q:
        x = q.popleft()
        if x == k:
            print(arr[x])
            break
        for i in range(3):
            if i != 2:
                nx = x + dx[i]
            else:
                nx = x * dx[i]
            if 0 <= nx <= 100000 and arr[nx]==0:
                q.append(nx)
                arr[nx] = arr[x] + 1

n, k = map(int,input().split())
arr = [0] * 1000001
bfs(n)