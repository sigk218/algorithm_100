import sys
sys.stdin = open('input.txt', 'r')

# 최대 최소 조건
n = int(input())
cnt = [0 for _ in range(n+1)]

for i in range(2, n+1):
    cnt[i] = cnt[i-1] + 1
    if i % 2 == 0:
        cnt[i] = min(cnt[i], cnt[i // 2] + 1)
    if i % 3 == 0:
        cnt[i] = min(cnt[i], cnt[i // 3] + 1)

print(cnt[n])

