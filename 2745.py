sentence = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

N, B = input().split()
N = N[::-1]
B = int(B)
ans = 0
for i in range(len(N)-1, -1, -1):
    ans += sentence.index(N[i]) * (B**i)

print(ans)