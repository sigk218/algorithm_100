# import sys
# sys.stdin = open('input.txt', 'r')

n = int(input())
dp = [0] * (n+1)

for i in range(2, n+1, 2):
    if i == 2:
        dp[i] = 3
        continue

    temp = 0
    for j in range(2, i-2, 2):
        temp += 2 * dp[j]
    dp[i] = 3 * dp[i - 2] + temp + 2

print(dp[n])