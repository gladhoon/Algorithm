import sys
input = sys.stdin.readline
k = int(input())
arr = []
for i in range(k):
    num = int(input())
    if num == 0:
        arr.pop(len(arr)-1)
    else:
        arr.append(num)

print(sum(arr))
