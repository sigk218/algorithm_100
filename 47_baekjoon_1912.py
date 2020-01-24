import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
numbers = list(map(int, map(int, input().split())))
temp = [0] * n
idx = 0

while idx < n:
    # print(temp[idx-1], numbers[idx])
    if temp[idx-1] + numbers[idx] > numbers[idx]:
        temp[idx] = temp[idx-1] + numbers[idx]
    else:
        temp[idx] = numbers[idx]
    idx += 1
# print(temp)
print(max(temp))
