while True:
    n = int(input())
    total = 0
    arr = []
    if n == -1:
        break
    for i in range(1,n):
        if n % i == 0:
            arr.append(i)
            total += i
    if total == n:
        print(n, '=', end=' ')
        for i in range(len(arr)):
            if i == len(arr)-1:
                print(arr[i])
            else:
                print(arr[i], '+', end=' ')
    else:
        print(n, 'is NOT perfect.')