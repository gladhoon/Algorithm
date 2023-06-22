black = [1, 1, 2, 2, 2, 8]
white = list(map(int, input().split()))
arr = []
for i in range(len(black)):
    arr.append(black[i] - white[i])

print(*arr)