import sys
n, h = map(int, input().split())
up = [0] * (h+1)
down = [0] * (h+1)

cnt = n
range_ = 0

for i in range(n):
    length = int(sys.stdin.readline())
    if (i+1)%2 == 0:
        up[length] += 1
    else:
        down[length] += 1

for i in range(h-1,0,-1):       # h가 1이면 1~(h-1)길이의 기둥들이 다 지가남 (누적합)
    up[i] += up[i+1]
    down[i] += down[i+1]

for i in range(1,h+1):          # 개똥벌레 지나가는 구간(높이) 1~h
    k = down[i] + up[h-i+1]     # 석순하고 종유석 겹치는 부분
    if cnt > k:
        cnt = k
        range_ = 1
    elif cnt == k:
        range_ += 1

print(cnt, range_)