A, B, V  = map(int, input().split())
snail, day = 0, 1

day = (V-B) // (A-B)
remain = (V-B) % (A-B)
if remain == 0:
    print(day)
else:
    print(day+1)