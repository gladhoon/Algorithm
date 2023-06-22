n = int(input())
start = 2

for i in range(1, n+1):
    start += start-1

print(start*start)