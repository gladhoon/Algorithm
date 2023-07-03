n = int(input())
coin = [500, 100, 50, 10]
ans = 0

for remain in coin:
    ans += n // remain
    n %= remain

print(ans)