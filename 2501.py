p, q = map(int, input().split())
arr = []

for i in range(1,p+1):
    if p % i == 0:
        arr.append(i)

if q > len(arr):
    print(0)
else:
    print(arr[q-1])