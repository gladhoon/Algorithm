X = int(input())
n = 1
while X > n:
    X -= n
    n += 1

if n % 2 == 1:
    x = n - X + 1
    y = X
else:
    x = X
    y = n - X + 1

print(x,'/',y,sep='')