arr = []
for _ in range(9):
    arr.append(list(map(int, input().split())))

ans, row, column = 0, 0, 0
for i in range(9):
    for j in range(9):
        if arr[i][j] >= ans:
            ans = arr[i][j]
            row = i
            column = j

print(ans)
print(row+1, column+1)