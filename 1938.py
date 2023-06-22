import math

n = int(input())
graph = []
B, E = [], []
for _ in range(n):
    graph.append(list(input()))

for i in range(n):
    if graph[i] in 'B':
        for j in range(n):
            if graph[i][j] == 'B':
                B.append((i,j))
print(B)