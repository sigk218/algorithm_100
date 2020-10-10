# 미로 탈출
import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(n)]

import collections

distance = [[0 for _ in range(m)] for _ in range(n)]
q = collections.deque()
# 1인 칸만 갈 수 있다
q.append((0, 0, 1))
distance[0][0] = 1

while q:
    x, y, d = q.popleft()
    for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
        xx = x + dx
        yy = y + dy
        if xx < 0 or xx >= n or yy < 0 or yy >= m:continue
        if arr[xx][yy] == 0: continue
        if distance[xx][yy]: continue
        distance[xx][yy] = d+1
        q.append((xx, yy, d+1))
print(distance[n-1][m-1])