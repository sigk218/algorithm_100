import sys
sys.stdin = open('input.txt', 'r')

# 이 성에있는 방의 개수 
# 가장 넓은 방의 넓이 
# 하나의 벽을 베거하여 얻을 수 있는 가장 넓은 방의 크기

import collections
def bfs(i, j, room):
    cnt = 0
    q = collections.deque()
    q.append((i, j))
    d[i][j] = room

    while q:
        x, y = q.popleft()
        cnt += 1
        for idx in range(4):
            xx = x + dir[idx][0]
            yy = y + dir[idx][1]
            if not (0 <= xx < n and 0 <= yy < m): continue
            if d[xx][yy] != 0: continue
            # 지금에서 갈 수 없는 방향이면
            if arr[x][y] & (1 << idx): continue
            d[xx][yy] = room
            q.append((xx, yy))
    return cnt

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
# 몇 번째 그룹인지 (visited)
d = [[0 for _ in range(m)] for __ in range(n)]
# 한 그룹당 몇개의 방이 있는지
area = [0 for _ in range(50*50+1)]
# 방향: 서, 북, 동, 남
dir = [(0, -1), (-1, 0), (0, 1), (1, 0)]

room, maxarea = 0, 0
for i in range(n):
    for j in range(m):
        if d[i][j]: continue
        room += 1
        temp = bfs(i, j, room)
        area[room] = temp
        maxarea = max(maxarea, temp)
# print(room, maxarea)
# print(*d, sep='\n')

answer = 0
for i in range(n):
    for j in range(m):
        for idx in range(4):
            xx = i + dir[idx][0]
            yy = j + dir[idx][1]
            if not (0 <= xx < n and 0 <= yy < m): continue
            # 같은 그룹에 속 할경우
            if d[xx][yy] == d[i][j]: continue
            # 벽인 경우에만
            if arr[i][j] & (1<<idx):
                answer = max(answer, area[d[i][j]] + area[d[xx][yy]])
print(room)
print(maxarea)
print(answer)
