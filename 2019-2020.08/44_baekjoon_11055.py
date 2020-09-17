import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
numbers = list(map(int, input().split()))
# cnt, sum
total = [0 for _ in range(n)]

for i in range(n):
    total[i] += numbers[i]
    for j in range(i):
        if numbers[i] > numbers[j] and total[j] + numbers[i] > total[i]:
                total[i] = total[j] + numbers[i]
    # print(total)
print(max(total))