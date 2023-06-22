import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    s = input().rstrip()
    s = s.split(' ')
    if s[0] == 'push':
        arr.append(int(s[1]))
    elif s[0] == 'pop':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[len(arr)-1])
            arr.pop(len(arr)-1)
    elif s[0] == 'size':
        print(len(arr))
    elif s[0] == 'empty':
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif s[0] == 'top':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[len(arr) - 1])
