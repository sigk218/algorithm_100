import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
numbers = list(map(int, input().split()))
cnt = [0] * n

for i in range(n):
    for j in range(i):
        # 나보다 작은 숫자들 중에 가장 긴 숫자
        if numbers[i] > numbers[j] and cnt[i] < cnt[j]:
            cnt[i] = cnt[j]
    cnt[i] += 1
print(max(cnt))