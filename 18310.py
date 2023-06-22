# 짝수 개일 경우, 두 점 사이에 모든 값이 정답이 된다. => 그래서 문제에서 가장 작은 값, 가장 큰 값을 구하라 주어짐
# 홀수 개일 경우, 가운데 점이 정답

n = int(input())
home = sorted(list(map(int, input().split())))

if n // 2 == 0:
    print(home[n//2])
else:
    print(home[(n-1)//2])