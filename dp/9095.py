def dfs(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return dfs(n-1) + dfs(n-2) + dfs(n-3)
t = int(input())
for test_case in range(1, t+1):
    m = int(input())
    print(dfs(m))