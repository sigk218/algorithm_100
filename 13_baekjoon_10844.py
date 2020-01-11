import sys
sys.stdin = open('input.txt', 'r')
# top-down과 buttom-up 풀이가 있다.
MOD = 1000000000
n = int(input())

dp = [[0] * 10 for _ in range(n+1)]
dp[1] = [0] + [1] * 9

for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][j+1]
            continue
        elif j == 9:
            dp[i][j] = dp[i-1][j-1]
            continue
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
    # print(dp)
print(sum(dp[n]) % MOD)