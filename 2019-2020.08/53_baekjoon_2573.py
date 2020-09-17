import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]

ice = dict()
for i in range(n):
    for j in range(m):
        if li[i][j] > 0:
            ice[(i, j)] = li[i][j]

year = 0
exit = False
while True:
    year += 1
    change = dict()
    for (x, y), tall in ice.items():
        zero = 0
        for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if li[nx][ny] == 0:
                    zero += 1
        # 녹일 것이 있을 때만 추가
        if zero > 0:
            change[(x, y)] = zero
    # 녹일것이 없으면 더 이상 쪼개지지 않음
    if len(change) == 0:
        print('0')
        break
    for (x, y), minus in change.items():
        ice[(x, y)] -= minus
        if ice[(x, y)] <= 0:
            li[x][y] = 0
            del ice[(x, y)]


    #  dfs로 확인하기
    # 다 녹을 때 까지 두 덩어리로 분리되지 않으면 0 을 출력한다
    cnt = 0
    visited = {(i, j): 0 for i in range(n) for j in range(m)}
    for (x, y), tall in ice.items():
        # print(x, y, tall)
        if visited[(x, y)] == 0:
            visited[(x, y)] = 1
            q = [(x, y)]
            # 2개 이상이면 조기 종료
            if cnt >= 2:
                exit = True
                break
            cnt += 1
            while q:
                tx, ty = q.pop()
                for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                    nx = tx + dx
                    ny = ty + dy
                    if 0 <= nx < n and 0 <= ny < m:
                        if ice.get((nx, ny)) and visited[(nx, ny)] == 0:
                            visited[(nx, ny)] = 1
                            q.append((nx, ny))
    if exit or cnt >= 2:
        print(year)
        break
    else:
        # print(cnt, ice)
        # 빙산이 다 녹았거나 하나만 남았을 경우
        if len(ice) <= 1:
            print(0)
            break


