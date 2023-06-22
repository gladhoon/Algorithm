import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    left = 0
    s = list(input())
    for i in s:
        if i == "(":
            left += 1
        elif i == ")":
            left -= 1
        if left < 0:
            print('NO')
            break
    if left == 0:
        print('YES')
    elif left > 0:
        print('NO')