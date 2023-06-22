import sys
input = sys.stdin.readline

arr = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num, B = map(int, input().split())
N = ''

while num != 0:
    N += str(arr[num % B])
    num //= B

N = N[::-1]
print(N)