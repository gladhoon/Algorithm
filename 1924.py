x, y = map(int, input().split())
week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

for i in range(1,x):
    if x == 1:
        continue
    elif i == 2:
        y += 28
    elif i == 4 or i == 6 or i == 9 or i == 11:
        y += 30
    else:
        y += 31

day = y % 7
print(week[day])