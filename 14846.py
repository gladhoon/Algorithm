import sys
input = sys.stdin.readline

arr = []
position = []

n = int(input())
for _ in range(n):
    arr.append(list(map(int, input().split())))

m = int(input())
for _ in range(m):
    position.append(list(map(int, input().split())))

for i in range(m):
    answer = []
    x1, y1, x2, y2 = position[i][0]-1, position[i][1]-1, position[i][2]-1, position[i][3]-1
    for y in range(y2-y1+1):
        for x in range(x2-x1+1):
            if arr[x][y] not in answer:
                answer.append(arr[x][y])
    print(len(answer))