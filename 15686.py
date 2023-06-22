from itertools import combinations
import math
n, m = map(int, input().split())
graph = []
chicken = []
house = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chicken.append([i,j])
        if graph[i][j] == 1:
            house.append([i,j])

answer = math.inf

for market in combinations(chicken, m):
    temp = 0
    for x,y in house:
        dist = math.inf
        for j in range(m):
            dist = min(dist, abs(x - market[j][0]) + abs(y - market[j][1]))
        temp += dist
    answer = min(answer, temp)

print(answer)