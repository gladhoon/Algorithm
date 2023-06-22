T = int(input())

coin = [25, 10, 5, 1]
for test_case in range(1, T+1):
    n = int(input())
    arr = []
    for i in range(len(coin)):
        arr.append(n//coin[i])
        n %= coin[i]

    print(*arr)