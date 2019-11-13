import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
dragons = [list(map(int, input().split())) for _ in range(n)] # x, y, d, g

directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]

result = [[0] * 101 for _ in range(101)]
# result = []

def draw(x, y, d, g):
    di_old = []
    di_new = []
    di_old.append(d)
    result[x][y] = 1
    tx, ty = x+directions[d][0], y+directions[d][1]
    result[tx][ty] = 1

    if g > 0:
        di_new.append((d + 1) % 4)
        tx, ty = tx+directions[(d + 1) % 4][0], ty+directions[(d + 1) % 4][1]
        result[tx][ty] = 1

    for gg in range(g-2+1):
        temp_d = []
        for old in di_old:
            temp_d.append((old+2) % 4)
            tx, ty = tx-directions[old][0], ty-directions[old][1]
            # result.append((tx, ty))
            result[tx][ty] = 1
        for new in di_new:
            temp_d.append(new)
            tx, ty = tx + directions[new][0], ty + directions[new][1]
            # result.append((tx, ty))
            result[tx][ty] = 1
        di_old += di_new
        di_new = temp_d

for y, x, d, g in dragons:
    draw(x, y, d, g)

visited = [[0] * 100 for _ in range(100)]
cnt = 0
for i in range(101):
    for j in range(101):
        if result[i][j]:
            for dx, dy in (0, 1), (1, 1), (1, 0):
                nx, ny = i+dx, j+dy
                if 0<= nx < 101 and 0 <= ny < 101:
                    if not result[nx][ny]:
                        break
                else:
                    break
            else:
                cnt += 1
print(cnt)


