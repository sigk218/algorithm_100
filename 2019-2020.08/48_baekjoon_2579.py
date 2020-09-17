import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
stairs = [int(input()) for _ in range(n)]
dp = [0] * n


for i in range(n):
    if i == 0:
        dp[i] = stairs[i]
        continue
    # 직전칸, 처음칸
    if i == 1:
        dp[i] = max(stairs[i] + stairs[i-1], stairs[i])
        continue
    dp[i] = max(stairs[i]+stairs[i-1]+dp[i-3], stairs[i] + dp[i-2])
print(dp[n-1])