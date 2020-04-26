import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
arr = [[0 for _ in range(n)] for __ in range(n)]

for _ in range(m):
    i, j = map(int, input().split())
    arr[i-1][j-1] = arr[j-1][i-1] = 1

# 3개의 조합이면 for문 3번 돌리면 된다
cnt = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if arr[i][j] or arr[j][k] or arr[k][i]:
                continue
            cnt += 1
print(cnt)

