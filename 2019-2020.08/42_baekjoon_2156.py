import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
# 0: 음료의 양 1: 이전 o, 이번 o 2: 이전 x, 이번 : o, 이번 : x
grape = [[0, 0, 0, 0] for _ in range(n)]
for nn in range(n):
    grape[nn][0] = int(input())

for nn in range(n):
    if nn == 0:
        grape[nn][1] = grape[nn][0]
        grape[nn][2] = grape[nn][0]
        continue
    grape[nn][1] = grape[nn-1][2] + grape[nn][0]
    grape[nn][2] = grape[nn-1][3] + grape[nn][0]
    grape[nn][3] = max(grape[nn-1][1], grape[nn-1][2], grape[nn-1][3])

print(max(grape[n-1]))