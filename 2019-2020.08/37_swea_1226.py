import sys, collections
sys.stdin = open('input.txt', 'r')


def solve(sx, sy):
    global flag
    q = collections.deque()
    q.append((sx, sy))
    miro[sx][sy] = 1

    while q:
        x, y = q.popleft()
        for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
            xx = x + dx
            yy = y + dy
            if 0 <= xx < n and 0 <= yy < n:
                if miro[xx][yy] == 0:
                    miro[xx][yy] = 1
                    q.append((xx, yy))
                elif miro[xx][yy] == 3:
                    flag = 1
                    return




T = 10
for _ in range(T):
    tc = int(input())

    n = 16
    miro = [list(map(int, input())) for _ in range(n)]

    #  출발점, 도착점 찾기
    sx, sy, ex, ey = 0, 0, 0, 0
    for i in range(n):
        for j in range(n):
            if sx != 0 and sy != 0 and ex != 0 and ey != 0:
                break
            elif miro[i][j] == 2:
                sx, sy = i, j
            elif miro[i][j] == 3:
                ex, ey = i, j
    # print(sx, sy, ex, ey)

    flag = 0
    solve(sx, sy)
    print('#{} {}'.format(tc, flag))