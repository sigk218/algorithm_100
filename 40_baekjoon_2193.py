import sys
sys.stdin = open('input.txt', 'r')

n = int(input())

dp = [[0] * 2 for _ in range(n+1)]

for i in range(1, n+1):
    if i == 1:
        dp[i][0] = 0
        dp[i][1] = 1
        continue
    if i == 2:
        dp[i][0] = 1
        dp[i][1] = 0
        continue
    dp[i][0] = dp[i-1][0] + dp[i-1][1]
    dp[i][1] = dp[i-1][0]
print(sum(dp[n]))