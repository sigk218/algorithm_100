import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
arr = [[0 for _ in range(2*n)] for __ in range(n)]
tile = [[0 for _ in range(2*n)] for __ in range(n)]

idx = 1
for i in range(0, n):
    s = 0 if i % 2 == 0 else 1
    for j in range(s, 2*n-1, 2):
        f, s = map(int, input().split())
        arr[i][j] = f
        arr[i][j+1] = s
        tile[i][j] = idx
        tile[i][j+1] = idx
        idx += 1

# print(*arr, sep='\n')
# print(*tile, sep='\n')

def samet(x1, y1, x2, y2):
    if tile[x1][y1] == tile[x2][y2]:return True
    else: return False


def bfs(i, j):
    visited = [[0 for _ in range(2*n)] for __ in range(n)]
    q = [(1, i, j)]
    visited[i][j] = 1
    # path[a] = b a 번은 b 번에서 부터 왔다
    path = [0 for _ in range(idx)]
    while q:
        d, x, y = q.pop(0)
        if tile[x][y] == idx-1:
            return d, path
        for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
            xx = x + dx
            yy = y + dy
            if 0 <= xx < n and 0 <= yy < 2*n and not visited[xx][yy] and arr[xx][yy]:
                if samet(x, y, xx, yy):
                    visited[xx][yy] = 1
                    q.append((d, xx, yy))
                else:
                    if arr[x][y] == arr[xx][yy]:
                        visited[xx][yy] = 1
                        path[tile[xx][yy]] = tile[x][y]
                        q.append((d+1, xx, yy))
    # 마지막 타일에 도달하지 못 했을 때 
    return d, path



(dep, tP) = bfs(0, 0)
for i in range(idx-1, -1, -1):
    if tP[i]:
        start = i
        break
answer = [start]
while tP[start] != 0:
    answer.append(tP[start])
    start = tP[start]
print(dep)
for i in range(len(answer)-1, -1, -1):
    print(answer[i], end=' ')

