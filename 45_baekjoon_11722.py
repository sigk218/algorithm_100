import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
numbers = list(map(int, input().split()))
dp = [0] * n

for i in range(n):
    for j in range(i):
        if numbers[i] < numbers[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))