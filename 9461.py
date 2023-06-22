# 이중 for문, 재귀함수 쓰면 런타임 error
p = []
p.extend([1, 1, 1])

for i in range(3,100):
    p.append(p[i-3] + p[i-2])

t = int(input())
for i in range(t):
    n = int(input())
    print(p[n-1])

# t = int(input())
# for i in range(t):
#     n = int(input())
#     if n-1 > len(p):
#         for j in range(len(p), n):
#             p.append(p[j-3] + p[j-2])
#         print(p[n-1])
#     else:
#         print(p[n-1])

