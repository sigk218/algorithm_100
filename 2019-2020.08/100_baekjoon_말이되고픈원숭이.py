import sys
sys.stdin = open('input.txt', 'r')

k = int(input())
m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

direction = [(-2, -1), (-1, -2), (1, -2), (2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1)]
dist = [[[0 for _ in range(k+1)] for __ in range(m)] for __ in range(n)]

import collections
def bfs():
    q = collections.deque()
    q.append((0, 0, 0))
    dist[0][0][0] = 1

    while q:
        x, y, cnt = q.popleft()
        # print(x, y, cnt)
        if x == n-1 and y == m-1:
            return dist[x][y][cnt]
        # 말 처럼 이동할 수 있으면
        if cnt+1 <= k:
            for (dx, dy) in direction:
                xx = x + dx
                yy = y + dy
                if 0 <= xx < n and 0 <= yy < m and not dist[xx][yy][cnt+1] and arr[xx][yy] == 0:
                    dist[xx][yy][cnt+1] = dist[x][y][cnt] + 1
                    q.append((xx, yy, cnt+1))
        for dx2, dy2 in (0, 1), (-1, 0), (0, -1), (1, 0):
            nx = x + dx2
            ny = y + dy2
            if 0 <= nx < n and 0 <= ny < m and not dist[nx][ny][cnt] and arr[nx][ny] == 0:
                dist[nx][ny][cnt] = dist[x][y][cnt] + 1
                q.append((nx, ny, cnt))

    return -1

answer = bfs()
print(answer if answer == -1 else answer-1)
