import sys
sys.stdin = open('input.txt', 'r')

# 가장 짧은 다리를 하나만 놓기로 하였다
# n * n

# 섬 찾기
# 다리 놓기 -> 가장 짧은 다리
# 1의 가장 외곽선에서 출발해서, 2를 만날때까지 BFS를 돌려서 가장 짧은 길이를 찾기

import collections
def find_land(xi, yi, num):
    global land_map

    result = [(xi, yi)]
    q = collections.deque()
    q.append((xi, yi))
    land_map[xi][yi] = num

    while q:
        x, y = q.popleft()
        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            xx = x + dx
            yy = y + dy
            if any([xx < 0, xx >= n, yy < 0, yy >= n]):
                continue
            # 바다거나, 이미 번호를 매긴 곳은 못감
            if land_map[xx][yy]:
                continue
            if arr[xx][yy] == 0:
                continue
            land_map[xx][yy] = num
            q.append((xx, yy))
            result.append((xx, yy))
    return result

def find_mini(xi, yi, num):
    global visited, answer

    q = collections.deque()
    q.append((xi, yi, 0))
    visited[xi][yi] = 0

    while q:
        x, y, d = q.popleft()
        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            xx = x + dx
            yy = y + dy
            if any([xx < 0, xx >= n, yy < 0, yy >= n]):
                continue
            # 이미 번호를 매긴 곳은 못감
            if visited[xx][yy]:
                continue

            if land_map[xx][yy] and land_map[xx][yy] != num:
                answer = min(answer, d)
                return
            visited[xx][yy] = d+1
            # 우리 구역일 경우
            if land_map[xx][yy] == num:
                q.append((xx, yy, d))
            else:
                q.append((xx, yy, d+1))

    return -1

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
land_map = [[0 for _ in range(n)] for _ in range(n)]
land_num = 0
start = []
for i in range(n):
    for j in range(n):
        if any([arr[i][j] == 0, land_map[i][j]]):continue
        # 땅인 곳에서만 시작한다
        land_num += 1
        t = find_land(i, j, land_num)
        start.append(t)

# bfs로 다른 섬 까지 최단거리를 찾는다
# 최단 거리를 갱신해준다
answer = 201
for i in range(land_num):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    for x, y in start[i]:
        if visited[x][y]:continue
        find_mini(x, y, i+1)

print(answer)