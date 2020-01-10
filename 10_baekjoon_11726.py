import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
cnt = [0 for _ in range(n+1)]
cnt[0] = 1
cnt[1] = 1



for i in range(2, n+1):
    cnt[i] = (cnt[i-1] + cnt[i-2]) % 1007

print(cnt[n])