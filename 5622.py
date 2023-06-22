arr = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
s = input()
time = 0
for i in range(len(s)):
    for j in arr:
        if s[i] in j:
            time += arr.index(j)+3

print(time)