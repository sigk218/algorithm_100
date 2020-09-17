import sys
sys.stdin = open('input.txt', 'r')

# 길이가 N인 오르막의 개수를 10007로 나눈 나머지를 출력한다

n = int(input())
# i 번째에서 j 값의 오르막의 수
dp = [[0] * 10 for _ in range(1001)]

for j in range(10):
    dp[0][j]
    dp[1][j] = 1
for i in range(2, n+1):
    for j in range(10):
        # 현재 자리수 보다 크거나 같은 값으로 만들 수 있다.
        for k in range(j+1):
            dp[i][j] += dp[i-1][k]
        dp[i][j] %= 10007
print(dp)
answer = 0
for j in range(10):
    answer += dp[n][j]
answer %= 10007
print(answer)


