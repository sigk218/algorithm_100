import sys
sys.stdin = open('input.txt', 'r')

# 가로나 세로중 지나갈 수 있는 칸이 있다면 ok -> 모든 칸을 다 검사 해야한다
# dfs를 돌면서 갯수가 바뀌었다면 ? 검사해보기 -> 하나라도 나오면 break
# 빙산이랑 비슷한듯

# 물과 닿아있다면 녹는다
def check():
    visited = [[0 for _ in range(m)] for __ in range(n)]
    q = collections.deque()
    q.append((x1, y1))
    visited[x1][y1] = 1

    while q:
        xx, yy = q.popleft()
        if xx == x2 and yy == y2:
            return True
        for dx, dy in (0, 1), (-1, 0), (0, -1), (1, 0):
            nx = xx + dx
            ny = yy + dy
            if not (0 <= nx < n and 0 <= ny < m): continue
            if visited[nx][ny]: continue
            if arr[nx][ny] == 'X':continue
            visited[nx][ny] = 1
            q.append((nx, ny))
    return False


import collections
n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

x1 = y1 = x2 = y2 = -1

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            if x1 == -1:
                x1, y1 = i, j
            else:
                x2, y2 = i, j
                break

def bfs(i, j):
    result = set()
    q = collections.deque()
    q.append((i, j))
    visited[i][j] = 1
    for dx, dy in (0, 1), (-1, 0), (0, -1), (1, 0):
        xi = i + dx
        yi = j + dy
        if 0 <= xi < n and 0<= yi < m and arr[xi][yi] == '.':
            result.add((i, j))
            break

    while q:
        x, y = q.popleft()
        # print(x, y)
        for dx, dy in (0, 1), (-1, 0), (0, -1), (1, 0):
            xx = x + dx
            yy = y + dy
            if 0 <= xx < n and 0 <= yy < m:
                if arr[xx][yy] == '.' or arr[xx][yy] == 'L':
                    result.add((x, y))
                elif arr[xx][yy] == 'X' and not visited[xx][yy]:
                    visited[xx][yy] = 1
                    q.append((xx, yy))
    return result

cnt = [-1]
if check():
    print(1)
    exit()

while True:
    nowcnt = 0
    visited = [[0 for _ in range(m)] for __ in range(n)]
    melt_lst = set()
    for i in range(n):
        for j in range(m):
            if visited[i][j]:continue
            if arr[i][j] == '.' or arr[i][j] == 'L': continue
            nowcnt += 1
            melt_lst.update(bfs(i, j))

    for x, y in melt_lst:
        arr[x][y] = '.'

    # print(*arr, sep='\n')
    if cnt[-1] == nowcnt:
        continue
    cnt.append(nowcnt)
    if check():
        break
print(len(cnt) -1)
