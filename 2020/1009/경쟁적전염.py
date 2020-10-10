import sys
sys.stdin = open('input.txt', 'r')

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
s, xi, yi = map(int, input().split())

xi -= 1
yi -= 1

import collections

virus = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 0: continue
        virus.append((arr[i][j], i, j, 0))

# 한 번 정렬해준다
virus.sort()
virus = collections.deque(virus)

while virus:

    num, x, y, d = virus.popleft()
    if d == s:
        break
    for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
        xx = x + dx
        yy = y + dy
        if xx < 0 or xx >= n or yy < 0 or yy >= n:continue
        if arr[xx][yy]:continue
        arr[xx][yy] = num
        virus.append((num, xx, yy, d+1))

print(arr[xi][yi])