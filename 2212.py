import sys
input = sys.stdin.readline

def sensor(arr, n, k):
    answer = 0
    broad = []
    arr.sort()
    if k >= n:
        answer = 0
        return answer
    for i in range(n-1):
        broad.append(arr[i+1]-arr[i])
    broad.sort()
    broad.reverse()
    for i in range(k-1):
        broad.pop(0)
    answer = sum(broad)
    return answer

a = int(input())
b = int(input())
array = list(map(int, input().split()))

print(sensor(array,a,b))