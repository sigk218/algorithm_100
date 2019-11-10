import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
cr, cc, d = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]

def wall(x, y):
    if 0 <= x < n and 0 <= y < m: return False
    else: return True

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def clean_area(i, j, di):
    cnt = 0
    q = []
    q.append((i, j, di))
    li[i][j] = 9
    cnt += 1

    while q:
        x, y, d = q.pop(0)
        for i in range(4):
            idx = (d - i + 3) % 4
            nx = x + directions[idx][0]
            ny = y + directions[idx][1]
            if not wall(nx, ny) and li[nx][ny] == 0:
                q.append((nx, ny, idx))
                cnt += 1
                li[nx][ny] = 9
                break
        else:
            nx = x-directions[d][0]
            ny = y-directions[d][1]
            if not wall(nx, ny) and li[nx][ny] != 1:
                q.append((nx, ny, d))
    return cnt


print(clean_area(cr, cc, d))

