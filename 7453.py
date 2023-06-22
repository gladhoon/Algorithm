import sys
input = sys.stdin.readline
n = int(input())
A, B, C, D, AB, CD = [], [], [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
for i in range(n):
    for j in range(n):
        AB.append(A[i] + B[j])
        CD.append(C[i] + D[j])
AB.sort()
CD.sort()

ans = 0
left, right = 0, len(CD)-1      # AB 시작점, CD 끝점

while left < len(AB) and right >= 0:
    if AB[left] + CD[right] == 0:
        i = left + 1
        j = right - 1
        while i < len(AB) and AB[left] == AB[i]:
            i += 1
        while j >= 0 and CD[right] == CD[j]:
            j -= 1
        ans += (i-left) * (right-j)
        left, right = i, j

    elif AB[left] + CD[right] > 0:
        right -= 1
    else:
        left += 1

print(ans)