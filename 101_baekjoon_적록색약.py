import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
arr = list(list(input()) for _ in range(n))
# 색약 아닌사람 
visited1 = [[0 for _ in range(n)] for __ in range(n)]
# 색약인 사람
visited2 = [[0 for _ in range(n)] for __ in range(n)]

import collections

def bfs1(x, y):
    if visited1[x][y]: return
    visited1[x][y] = 1

    q1 = collections.deque()

    q1.append((x, y))

    while q1:
        i, j = q1.popleft()
        for dx, dy in (0, 1), (-1, 0), (0, -1), (1, 0):
            ii = i + dx
            jj = j + dy
            if 0 <= ii < n and 0 <= jj < n and not visited1[ii][jj] and arr[ii][jj] == arr[x][y]:
                visited1[ii][jj] = 1
                q1.append((ii, jj))
    return 1

def bfs2(x, y):
    if visited2[x][y]: return
    visited2[x][y] = 1

    q = collections.deque()

    q.append((x, y))

    while q:
        i, j = q.popleft()
        for dx, dy in (0, 1), (-1, 0), (0, -1), (1, 0):
            ii = i + dx
            jj = j + dy
            if 0 <= ii < n and 0 <= jj < n and not visited2[ii][jj]:
                if arr[x][y] == 'R' or arr[x][y] == 'G':
                    if arr[ii][jj] == 'R' or arr[ii][jj] == 'G':
                        visited2[ii][jj] = 1
                        q.append((ii, jj))
                else:
                    if arr[x][y] == arr[ii][jj]:
                        visited2[ii][jj] = 1
                        q.append((ii, jj))
    return 1

answer1 = answer2 = 0
for i in range(n):
    for j in range(n):
        if not visited1[i][j]:
            answer1 += bfs1(i, j)
        if not visited2[i][j]:
            answer2 += bfs2(i, j)
print(answer1, answer2)