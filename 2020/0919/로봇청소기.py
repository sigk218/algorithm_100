import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
xi, yi, di = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]


import collections
q = collections.deque([(xi, yi, di)])
# arr[xi][yi] = 8

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

cnt = 1
while q:
    x, y, d = q.popleft()
    arr[x][y] = 8
    # 현재 위치 청소
    for i in range(1, 5):
        next_d = (d - i + 4) % 4
        xx = x + direction[next_d][0]
        yy = y + direction[next_d][1]
        if xx < 0 or xx >= n or y < 0 or y >= m:
            continue
        if arr[xx][yy]:
            continue
        # 왼쪽에 존재 한다면
        if arr[xx][yy] == 0:
            # arr[xx][yy] = 8
            # cnt += 1
            q.append((xx, yy, next_d))
            break
    else:
        xx = x - direction[d][0]
        yy = y - direction[d][1]
        # 뒤 쪽으로 못가면 작동을 멈춘다
        if xx < 0 or xx >= n or yy < 0 or yy >= m:
            break
        # 모두 벽 이라면 작동을 멈춘다
        if arr[xx][yy] == 1:
            break
        # !!!!!!!! 뒤 쪽 방향은 청소한 곳도 갈 수 있다 !!!!!!!!!!
        if arr[xx][yy] == 0 or arr[xx][yy] == 8:
            q.append((xx, yy, d))

answer = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 8:
            answer += 1
print(answer)

# print(cnt)