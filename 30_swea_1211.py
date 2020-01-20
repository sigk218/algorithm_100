import sys
sys.stdin = open('input.txt', 'r')

def inbox(x, y):
    if 0 <= x < 100 and 0 <= y < 100: return True
    else: return False

def go(x, y, direction):
    cnt = 0
    dy = -1
    if direction == 1:
        dy = 1

    # 1 : 오른쪽, 0 : 왼쪽
    while inbox(x, y) and ladder[x][y] == 1:
        cnt += 1
        y += dy
    return cnt-1, x, y-dy

def solve(sx, sy):
    cnt = 0
    while inbox(sx, sy) and sx >= 1:
        sx -= 1
        cnt += 1
        # 오른 쪽 체크 하기
        if inbox(sx, sy+1) and ladder[sx][sy+1] == 1:
            temp, sx, sy = go(sx, sy+1, 1)
            cnt += temp
        # 왼 쪽 체크 하기
        elif inbox(sx, sy-1) and ladder[sx][sy-1] == 1:
            temp, sx, sy = go(sx, sy-1, 0)
            cnt += temp
    return cnt, sx, sy

T = 10
for tc in range(T):
    n = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    endpoints = []
    for i in range(100):
        if ladder[99][i] == 1:
            endpoints.append((99, i))
    # print(endpoints)

    answer = []
    for x, y in endpoints:
        teml, tempx, tempy = solve(x, y)
        answer.append((teml, tempy))
    print('#{} {}'.format(tc+1, sorted(answer)[0][1]))
