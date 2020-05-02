import sys
sys.stdin = open('input.txt', 'r')

# 빨간 구슬을 구멍을통해 빼냄
# 보드에 구멍이 하나 있따
# 게임이 실패하는 경우 -1 을 출력한다
# 1. 파란 구슬이 구멍에 들어가면 x 2. 동시에 빠져도 실패  3.더이상 구슬이 움직이지 x
# 중력

n, m = map(int, input().split())
arr = list(list(input()) for _ in range(n))

################### DAY 9, 백준 코드랑 비교
rx = ry = bx = by = gx = gy = 0
for i in range(n):
    for j in range(m):
        # 빨간 공
        if arr[i][j] == 'R':
            rx, ry = i, j
            arr[i][j] = '.'
        # 파란 공
        elif arr[i][j] == 'B':
            bx, by = i, j
            arr[i][j] = '.'
        elif arr[i][j] == 'O':
            gx, gy = i, j
# print(gx, gy)
def inbox(x, y):
    if 0 <= x < n and 0 <= y < m and arr[x][y] != '#':
        return True
    else:
        return False

def gravity(x, y, dx, dy):

    while True:
        # 벽을 만나서 멈추면
        if not inbox(x, y):
            x -= dx
            y -= dy
            return x, y
        if x == gx and y == gy:
            return x, y
        x += dx
        y += dy


def bfs(ri, rj, bi, bj):
    visited = {(i, j, ii, jj): 0 for i in range(n) for j in range(m) for ii in range(n) for jj in range(m)}
    visited[(ri, rj, bi, bj)] = 1
    q = [(0, ri, rj, bi, bj)]
    while q:
        d, rx, ry, bx, by = q.pop(0)
        # if d > 10: return -1
        # print(d, rx, ry, bx, by)
        for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
            red = gravity(rx, ry, dx, dy)
            blue = gravity(bx, by, dx, dy)
            nrx, nry = red[0], red[1]
            nbx, nby = blue[0], blue[1]
            # 두 개다 빠진 경우
            if arr[nrx][nry] == 'O' and arr[nbx][nby] == 'O':
                continue
            # 두 개 좌표가 같을 경우
            # 더 가까이 있던 공을 위치로
            if red == blue:
                reddis = abs(rx-nrx) + abs(ry-nry)
                bluedis = abs(bx-nbx) + abs(by-nby)
                if reddis > bluedis:
                    nrx -= dx
                    nry -= dy
                else:
                    nbx -= dx
                    nby -= dy

            # 파란공만 빠진 경우
            if arr[nrx][nry] != 'O' and arr[nbx][nby] == 'O':
                continue
            # 빨간공이 빠졌을 경우
            if arr[nrx][nry] == 'O' and arr[nbx][nby] != 'O':
                return d+1
            if rx == nrx and ry == nry and bx == nbx and by == nby:continue
            if visited[(nrx, nry, nbx, nby)]: continue
            visited[(nrx, nry, nbx, nby)] = 1
            q.append((d+1, nrx, nry, nbx, nby))
    return -1


print(bfs(rx, ry, bx, by))
# 뭐부터 검사해야하는지 순서가 무척 중요했다
# 아... visited 체크를 안했다..바보다 바보 ..