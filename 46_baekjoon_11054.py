import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
numbers = list(map(int, input().split()))
# 증가, 감소
dp = [[0, 0] for _ in range(n)]

for i in range(n):
    for j in range(i):
        if numbers[i] > numbers[j] and dp[i][0] < dp[j][0]:
            dp[i][0] = dp[j][0]
    dp[i][0] += 1

for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if numbers[i] > numbers[j] and dp[i][1] < dp[j][1]:
            dp[i][1] = dp[j][1]
    dp[i][1] += 1

answer = 0
for i in range(n):
    answer = max(sum(dp[i]), answer)
print(answer-1)
