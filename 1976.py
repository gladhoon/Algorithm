import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
node = list(i for i in range(n))
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
route = list(map(int,input().split()))

def find(a):
    if node[a] != a:
        node[a] = find(node[a])
    return node[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        node[a] = b
    else:
        node[b] = a

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            union(i,j)

answer = 'YES'
for i in range(1,m):
    if node[route[i]-1] != node[route[0]-1]:
        answer = 'NO'
        break
print(answer)