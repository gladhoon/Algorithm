import sys
input = sys.stdin.readline
n, m, d = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
graph.append([0]*n)


def archer():
    for i in range(m):
        for j in range(i+1, m):
            for k in range(j+1, m):

