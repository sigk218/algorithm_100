import sys
sys.stdin = open('input.txt')

n = int(input())
# 1로 만들 수 있는 값으로 초기화
dp = [i for i in range(n+1)]

for i in range(2, n+1):
    for j in range(2, int(i ** 0.5) + 1):
        dp[i] = min(dp[i], dp[i-j*j]+1)
print(dp[n])