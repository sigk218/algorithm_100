import sys
sys.stdin = open('input.txt', 'r')

n = int(input())

cnt = [0 for _ in range(n+1)]

for i in range(1, n+1):
    if i == 1:
        cnt[i] = 1
        continue
    elif i == 2:
        cnt[i] = 3
        continue
    cnt[i] = (cnt[i-1] + 2 * cnt[i-2]) % 10007

print(cnt[n])