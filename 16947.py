import sys
from collections import deque
sys.setrecursionlimit(10**5)

#순환역 확인
def cycle_station(start, index, cnt):
    global isCycle
    visited[index] = True

    if start == index and cnt >= 2:
        isCycle = True
        return

    for i in station[index]:
        if isCycle:
            return
        if not visited[i]:
            cycle_station(start, i, cnt+1)
        elif i == start and cnt >= 2:
            cycle_station(start, i, cnt)
    return

#역과 순환역 사이 거리
def dist_station():
    global answer
    q = deque()

    for i in range(n):    #순환선 안에 있는 역
        if cycle[i]:
            answer[i] = 0
            q.append(i)

    while q:
        current = q.popleft()
        for j in station[current]:
            if answer[j] == -1:
                q.append(j)
                answer[j] = answer[current] + 1
    print(*answer)

        
n = int(input())
station = [[] for _ in range(n)]   #역 구간정보(간선)
cycle = [False] * n   #순환역 표시
answer = [-1] * n

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    station[a-1].append(b-1)
    station[b-1].append(a-1)

for i in range(n):
    visited = [False] * n
    isCycle = False
    cycle_station(i, i, 0)
    if isCycle:
        cycle[i] = True
dist_station()