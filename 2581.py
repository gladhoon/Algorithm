m = int(input())
n = int(input())
arr = []

for i in range(m,n+1):
    flag = False
    if i > 1:
        for j in range(2,i):
            if i % j == 0:
                flag = True
                break
        if flag is False:
            arr.append(i)

if len(arr) > 0:
    print(sum(arr))
    print(arr[0])
else:
    print(-1)