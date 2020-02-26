# 행과 열을 1부터 시작
# 파이프는 회전 가능, 3방향이 가능
# 파이프의 이동
# 1. 밀어서 이동 (오른쪽, 오른쪽 아래, 아래)
#  1-1. 한번에 45도만 회전 가능
# 가로 -> 오른쪽, 오른쪽 아래
# 세로 -> 아래, 오른쪽 아래
# 대각선 -> 오른쪽, 오른쪽아래, 아래
# 2. 벽에 닿으면 안됨, 빈칸만 차지해야함
# 파이프의 한쪽 끝을 (N,N)로 이동시키는 방법
# 처음 파이프는 (1, 1)과 (1, 2)를 차지

import sys, collections
sys.stdin = open('input.txt', 'r')

n = int(input())
dp = [[[0] * (n+1) for _ in range(n+1)] for __ in range(3)]

li = [list(map(int, input().split())) for _ in range(n)]

dp[0][0][1] = 1
for i in range(n):
    for j in range(1, n):
        # 가로로 가기
        if j+1 < n and li[i][j+1] == 0:
            dp[0][i][j+1] = dp[0][i][j] + dp[2][i][j]
        # 세로로 가기
        if i+1 < n and li[i+1][j] == 0:
            dp[1][i+1][j] = dp[1][i][j] + dp[2][i][j]
        # 대각선으로 가기
        if i+1 < n and j+1 < n and li[i+1][j+1] == 0 and li[i][j+1] == 0 and li[i+1][j] == 0:
            dp[2][i+1][j+1] = dp[0][i][j] + dp[1][i][j] + dp[2][i][j]


print(dp[0][n-1][n-1]+dp[1][n-1][n-1]+dp[2][n-1][n-1])