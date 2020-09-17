import sys
sys.stdin = open('input.txt', 'r')

r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]

visited = [[0 for _ in range(c)] for __ in range(r)]

totalwolf = totalsheep = 0
for i in range(r):
    for j in range(c):
        if visited[i][j] : continue
        visited[i][j] = 1
        if arr[i][j] == '#' :continue
        # v 나 o인 경우에만 경로 탐색
        sheep = wolf = 0
        if arr[i][j] == 'v': wolf +=1
        elif arr[i][j] == 'o' : sheep +=1
        q = [(i, j)]
        while q:
            x, y = q.pop(0)
            # print(x, y)
            for dx, dy in (0, 1), (-1, 0), (0, -1), (1, 0):
                xx = x + dx
                yy = y + dy
                if 0 <= xx < r and 0 <= yy < c and arr[xx][yy] != '#' and not visited[xx][yy]:
                    visited[xx][yy] = 1
                    q.append((xx, yy))
                    if arr[xx][yy] == 'v': wolf += 1
                    elif arr[xx][yy] == 'o': sheep += 1
        if wolf < sheep:
            totalsheep += sheep
        else:
            totalwolf += wolf

print(totalsheep, totalwolf)


