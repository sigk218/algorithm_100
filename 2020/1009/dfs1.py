# 음료수 얼려먹기
import sys
sys.stdin = open('input.txt', 'r')

def dfs(x, y, visited):

    if visited[x][y]:
        return
    visited[x][y] = 1

    for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
        xx = dx + x
        yy = dy + y
        if xx < 0 or xx >= n or yy < 0 or yy >= m:
            continue
        if arr[xx][yy]:continue
        dfs(xx, yy, visited)



n, m = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(n)]

visited = [[0 for _ in range(m)] for _ in range(n)]

answer = 0
for i in range(n):
    for j in range(m):
        if visited[i][j]:continue
        if arr[i][j]:continue
        print(i, j)
        dfs(i, j, visited)
        answer += 1
print(answer)

