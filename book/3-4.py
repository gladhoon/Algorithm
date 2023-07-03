n, k = map(int, input().split())
ans = 0
while n >= k:
    while n % k != 0:
        n -= 1
        ans += 1
    n //= k
    ans += 1

while n > 1:
    n -= 1
    ans += 1

print(ans)