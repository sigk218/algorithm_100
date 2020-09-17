# https://www.acmicpc.net/problem/16236



# 가는 것과, 먹는것을 분리해서 생각헀어야했는데 .. ㅜㅜ

# 먼저 아기상어까지 도달할 수 있는 최단 거리를 구한다
# 거리가 짧은 것 순서대로 먹는다

# 문제좀 똑바로 읽자..
# -> 먹은 상어의 나이 만큼 나이를 먹는줄 알았다..(상어의 속성, 속성마다 특징)
# 아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다.

import sys
sys.stdin = open('input.txt', 'r')
n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

sx, sy = 0, 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            arr[i][j] = 0
            sx, sy = i, j
            break

import collections
def bfs(xi, yi):
    global size
    # 각 물고기 까지의 최단 거리를 구한다, 위쪽(x) 왼쪽(y)
    # 거리를 저장
    fish = []
    distance = [[0 for _ in range(n)] for _ in range(n)]
    
    q = collections.deque([(xi, yi, 0)])
    distance[xi][yi] = 1

    while q:
        x, y, d = q.popleft()
        for dx, dy in (0, -1), (-1, 0), (0, 1), (1, 0):
            xx = x + dx
            yy = y + dy
            if xx < 0 or xx >= n or yy < 0 or yy >= n:
                continue
            if arr[xx][yy] > size:
                continue
            if distance[xx][yy]:
                continue

            distance[xx][yy] = d+1
            q.append((xx, yy, d+1))
            # 나보다 작은 것만 먹을 수 있다
            if 0 < arr[xx][yy] < size:
                fish.append((d+1, xx, yy))
    return fish


# 초반 아기 상어 크기 2
size = 2
num, answer = 0, 0
while True:
    temp = bfs(sx, sy)

    if temp:
        # 거리, 위쪽, 왼쪽 기준으로 정렬
        temp.sort(key = lambda x:[x[i] for i in range(3)])
        (second, nx, ny)= temp[0]
        answer += second

        # 초기화
        arr[nx][ny] = 0
        sx, sy = nx, ny

        # 지금까지
        num += 1

        if num == size:
            size += 1
            num = 0
    else:
        break

print(answer)