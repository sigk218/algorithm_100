import sys
sys.stdin = open('input.txt', 'r')

# 벽을 K개 까지 부수고 이동해도 된다.

n, m, k = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(n)]
# print(arr)

# i, j , k 까지 오는데 걸린 최단 경로
dist = [[[0 for ___ in range(k+1)] for _ in range(m)] for __ in range(n)]

import collections
def bfs():
    q = collections.deque()
    q.append((0, 0, 0))
    dist[0][0][0] = 1

    while q:
        x, y, kk = q.popleft()
        if x == n-1 and y == m-1:
            return dist[x][y][kk]
        for dx, dy in (0, 1), (-1, 0), (0, -1), (1, 0):
            xx = x + dx
            yy = y + dy
            if 0 <= xx < n and 0 <= yy < m and not dist[xx][yy][kk]:
                # 깍을 수 있는 경우
                if kk+1 <= k and arr[xx][yy] == 1:
                    dist[xx][yy][kk+1] = dist[x][y][kk] + 1
                    q.append((xx, yy, kk+1))
                if arr[xx][yy] == 0:
                    dist[xx][yy][kk] = dist[x][y][kk] + 1
                    q.append((xx, yy, kk))
    return -1

print(bfs())