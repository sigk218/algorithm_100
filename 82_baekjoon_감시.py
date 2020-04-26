import sys
sys.stdin = open('input.txt', 'r')

# cctv는 90도 회전 시킬 수 있고, 감시하려고 하는 방향이 가로 또는 세로 방향
# 사각지대 : cctv 가 감시할 수 없는 영역 (0으로 표시)
# 사각지대의 최소를 구하면 ?

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

cctv = {}
for i in range(n):
    for j in range(m):
        # arr[i][j] = 6 : 벽, arr[i][j] = 1 ~ 5 : cctv
        if 1 <= arr[i][j] <= 5:
            cctv[(i, j, arr[i][j])] = -1

# cctv 방향의 모든 경우의수 구하기
direction = {
    1: [[(0, 1)], [(0, -1)], [(1, 0)], [(-1, 0)]],
    2: [[(1, 0), (-1, 0)], [(0, 1), (0, -1)]],
    3: [[(-1, 0), (0, 1)], [(0, 1), (1, 0)], [(1, 0), (0, -1)], [(0, -1), (-1, 0)]],
    4: [[(0, -1), (-1, 0), (0, 1)], [(-1, 0), (0, 1), (1, 0)], [(0, 1), (1, 0), (0, -1)], [(1, 0), (0, -1), (-1, 0)]],
    5: [[(0, 1), (1, 0), (0, -1), (-1, 0)]],
}

def inbox(x, y):
    if 0 <= x < n and 0 <= y < m: return True
    else: return False

def watch():
    t = []
    for (x, y, num), check in cctv.items():
        for dx, dy in direction[num][check]:
            xx, yy = x, y
            while True:
                xx += dx
                yy += dy
                if not inbox(xx, yy) or arr[xx][yy] == 6:
                    break
                if 1 <= arr[xx][yy] <= 5: continue
                arr[xx][yy] = 8
                t.append((xx, yy))
    return t


def dfs(d):
    global answer
    if d == cctvnum:
        change_list = watch()
        cnt = 0
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 0:
                    cnt += 1
        answer = min(answer, cnt)
        for x, y in change_list:
            arr[x][y] = 0

    else:
        for (x, y, num), check in cctv.items():
            if check > -1: return
            for i in range(len(direction[num])):
                cctv[(x, y, num)] = i
                dfs(d+1)
                cctv[(x, y, num)] = -1
answer = 8 * 8 + 1
cctvnum = len(cctv)
dfs(0)
print(answer)
