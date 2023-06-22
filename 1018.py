n, m = map(int, input().split())

mtr = []
cnt = []
for i in range(n):
    mtr.append(input())

for a in range(n-7):
    for b in range(m-7):
        w_cnt = 0
        b_cnt = 0
        for i in range(a, a + 8):
            for j in range(b, b + 8):
                if (i + j) % 2 == 0:  # 짝수인 경우
                    if mtr[i][j] != 'W':  # W가 아니면, 즉 B이면
                        w_cnt += 1  # W로 칠하는 갯수
                    else:  # W일 때
                        b_cnt += 1  # B로 칠하는 갯수
                else:  # 홀수인 경우
                    if mtr[i][j] != 'W':  # W가 아니면, 즉 B이면
                        b_cnt += 1  # B로 칠하는 갯수
                    else:
                        w_cnt += 1  # W로 칠하는 갯수
        cnt.append(w_cnt)  # W로 시작할 때 경우의 수
        cnt.append(b_cnt)  # B로 시작할 때 경우의 수

print(min(cnt))
