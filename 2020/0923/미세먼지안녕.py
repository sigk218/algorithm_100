import sys
sys.stdin = open('input.txt', 'r')

# 입력
r, c, t = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(r)]

# 공기 청정기의 위치 찾기
machine = []
for i in range(r):
    if arr[i][0] == -1:
        # 무조건 위 쪽 값부터 오게된다.
        machine.append((i, 0))

def spread():
    # 이번에 퍼지게 될 먼지 리스트
    dust = []
    for i in range(r):
        for j in range(c):
            if arr[i][j] > 0:
                # 네 방향에 대해서 체크 하기
                # 몇 개의 칸으로 퍼질 수 있는지
                cnt = 0
                for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
                    xx = i + dx
                    yy = j + dy
                    # 벽을 나가면 x
                    if xx < 0 or xx >= r or yy < 0 or yy >= c:
                        continue
                    # 공기 청정기가 있으면 x
                    if arr[xx][yy] == -1:
                        continue
                    cnt += 1
                    dust.append((xx, yy, arr[i][j] // 5))
                arr[i][j] -= (arr[i][j] // 5) * cnt

    for x, y, d in dust:
        # print(x, y, d)
        arr[x][y] += d


def work():
    # 공기 청정기 위 쪽은 반시계 방향
    mx, my = machine[0]
    # 거꾸로 가서 한 칸씩 앞으로 당기면 된다
    x, y = mx, my
    temp = 0
    for dx, dy in (0, 1), (-1, 0), (0, -1), (1, 0):
        while True:
            x += dx
            y += dy
            if x < 0 or x >= r or y < 0 or y >= c:
                x -= dx
                y -= dy
                break
            if arr[x][y] == -1:
                break
            next = arr[x][y]
            arr[x][y] = temp
            temp = next


    # 공기 청정기 아래 쪽은 시계 방향
    mx, my = machine[1]
    # 거꾸로 가서 한 칸씩 앞으로 당기면 된다
    x, y = mx, my
    temp = 0
    for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
        while True:
            x += dx
            y += dy
            if x < 0 or x >= r or y < 0 or y >= c:
                x -= dx
                y -= dy
                break
            if arr[x][y] == -1:
                break
            next = arr[x][y]
            arr[x][y] = temp
            temp = next

for _ in range(t):
    spread()
    work()

answer = 0
for i in range(r):
    for j in range(c):
        if arr[i][j] > 0:
            answer += arr[i][j]
print(answer)