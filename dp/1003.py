zero = [1, 0, 1]
one = [0, 1, 1]
def dfs(n):
    m = len(zero)
    if n >= m:
        for i in range(m,n+1):
            zero.append(zero[i-2] + zero[i-1])
            one.append(one[i-2] + one[i-1])
    print(zero[n], one[n], sep=' ')

T = int(input())
for test_case in range(1,T+1):
    t = int(input())
    dfs(t)