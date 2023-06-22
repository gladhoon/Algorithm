import sys
input = sys.stdin.readline
while True:
    s = input().rstrip()
    flag = 1
    if s == '.':
        break
    arr = []
    for i in s:
        if i =='(' or i == '[':
            arr.append(i)
        elif i == ')':
            if not arr or arr[-1] == '[':
                flag = 0
                break
            elif arr[-1] == '(':
                arr.pop()
        elif i == ']':
            if not arr or arr[-1] == '(':
                flag = 0
                break
            elif arr[-1] == '[':
                arr.pop()
    if flag == 1 and not arr:
        print('yes')
    else:
        print('no')