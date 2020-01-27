import sys, collections
sys.stdin = open('input.txt', 'r')
def solve():
    visited = {(i, j, ii, jj) : 0 for i in range(n) for j in range(m) for ii in range(n) for jj in range(m)}
    q = collections.deque()
    q.append((rx, ry, bx, by, 0))
    visited[(rx, ry, bx, by)] = 1
    while q:
        currx, curry, curbx, curby, cnt = q.popleft()
        # print(currx, curry, curbx, curby, cnt)
        if cnt > 10: return -1
        if board[currx][curry] == 'O' and board[curbx][curby] != 'O':
            # print(currx, curry, curbx, curby, cnt)
            return cnt
        for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
            nextrx, nextry = currx, curry
            nextbx, nextby = curbx, curby
            # print(nextrx, nextry, currx, curry)
            while True:
                if board[nextbx][nextby] != '#' and board[nextbx][nextby] != 'O':
                    nextbx += dx
                    nextby += dy
                # 만약 갈 수 없는 경우
                else:
                    # 벽이면 한 칸 되돌린다.
                    if board[nextbx][nextby] == '#':
                        nextbx -= dx
                        nextby -= dy
                    break
            while True:
                if board[nextrx][nextry] != '#' and board[nextrx][nextry] != 'O':
                    nextrx += dx
                    nextry += dy
                # 만약 갈 수 없는 경우
                else:
                    # 벽이면 탈출
                    if board[nextrx][nextry] == '#':
                        nextrx -= dx
                        nextry -= dy
                    break
            if nextbx == nextrx and nextby == nextry:
                if board[nextrx][nextry] != 'O':
                    if abs(nextbx - curbx) + abs(nextby - curby) > abs(nextrx - currx) + abs(nextry - curry):
                        nextbx -= dx
                        nextby -= dy
                    else:
                        nextrx -= dx
                        nextry -= dy
            if not visited[(nextrx, nextry, nextbx, nextby)]:
                visited[(nextrx, nextry, nextbx, nextby)] = 1
                # print(nextrx, nextry, nextbx, nextby, cnt)
                q.append((nextrx, nextry, nextbx, nextby, cnt+1))
    return -1


n, m = map(int, input().split())
board = [list(input())for _ in range(n)]

rx, ry, bx, by = 0, 0, 0, 0
hx, hy = 0, 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            rx, ry = i, j
        elif board[i][j] == 'B':
            bx, by = i, j

print(solve())

