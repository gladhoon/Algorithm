n = int(input())
result = 0

while True:
    if n % 5 == 0:
        result += n // 5
        break
    else:
        if n >= 3:
            n -= 3
            result += 1
        else:
            result = -1
            break
print(result)