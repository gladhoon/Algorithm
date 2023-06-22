n = int(input())
for i in range(1, n+1):
    ans = 0
    share = i
    while True:
        if share == 0:
            break
        else:
            remain = share % 10
            ans += remain
            share //= 10
    if ans + i == n:
        print(i)
        n = 0
        break
if n != 0:
    print(0)