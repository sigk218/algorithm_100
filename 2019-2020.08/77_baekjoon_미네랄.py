import sys
sys.stdin = open('input.txt', 'r')

def wall(x, y):
    if 0 <= x < r and 0 <= y < c: return False
    else: return True

def findC(x, y):

    # if visited[x][y] : return
    bottom = [-1 for _ in range(c)]
    clu = []
    q = [(x, y)]
    arr[x][y] = '.'
    visited[x][y] = 1
    while q:
        xx, yy = q.pop(0)
        clu.append((xx, yy))
        # 다음이 바닥이면 바닥을 업데이트 해준다
        if wall(xx + 1, yy) or (not wall(xx + 1, yy) and arr[xx + 1][yy] == '.' and not visited[xx + 1][yy]):
            bottom[yy] = max(bottom[yy], xx)
            # print(bottom, yy, xx)
        for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
            nx, ny = xx + dx, yy + dy
            if not wall(nx, ny) and arr[nx][ny] == 'x' and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = 1
                arr[nx][ny] = '.'

    now = -1
    # print(bottom, clu)
    for i in range(c):
        if bottom[i] == -1:
            continue
        xx, yy = bottom[i], i
        while True:
            xx += 1
            if wall(xx, yy):
                xx -= 1
                break
            if arr[xx][yy] == 'x':
                xx -= 1
                break
        # print(bottom[i], xx)
        if now == -1:
            now = xx-bottom[i]
        else:
            now = min(now, xx-bottom[i])
    for xx, yy in clu:
        arr[xx+now][yy] = 'x'



r, c = map(int, input().split())
arr = list(list(input()) for _ in range(r))
# 던지는 횟수
n = int(input())
d = list(map(int, input().split()))
for i in range(n):
    d[i] = r - d[i]

# 0, 2, 4 -> 왼쪽에서 오른쪽으로
for i in range(n):
    if i % 2 == 0:
        for j in range(c):
            if arr[d[i]][j] == 'x':
                arr[d[i]][j] = '.'
                # print(d[i], j)
                break
    else:
        for j in range(c-1, -1, -1):
            if arr[d[i]][j] == 'x':
                arr[d[i]][j] ='.'
                # print(d[i], j)
                break

    visited = [[0 for _ in range(c)] for __ in range(r)]
    for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
       if not wall(d[i]+dx, j+dy) and arr[d[i]+dx][j+dy] == 'x':
           # 떨어 졌는 지 안 떨어졌는지 확인을 해주는 거!
           # 중복이 되면 x, y만 떨어지는 일이 발생함 !
           if visited[d[i]+dx][j+dy]:
               continue
           else:
               findC(d[i]+dx, j+dy)

for i in range(r):
    for j in range(c):
        print(arr[i][j], end='')
    print()


# 1. 바닥에 닿는것
# 2. visited 초기화 시점
# 3. bottom을 담아 주는 것