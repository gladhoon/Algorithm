n, k = map(int, input().split())
wv = [[0,0]]
knapsack = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(n):
    w,v = map(int, input().split())
    wv.append([w,v])

for i in range(1, n+1):
    for j in range(1, k+1):     #weight가 주어진 k 값보다 커질 문제는 생각할 필요 X
        w = wv[i][0]
        v = wv[i][1]

        if j < w:
            knapsack[i][j] = knapsack[i-1][j]
        else:
            knapsack[i][j] = max(v + knapsack[i-1][j-w], knapsack[i-1][j])

print(knapsack[n][k])