import sys
sys.stdin = open('input.txt', 'r')


# 최 단 거리니까 bfs로
import collections
def solve(icnt, iredx, iredy, ibluex, ibluey):

    q = collections.deque()
    q.append((icnt, iredx, iredy, ibluex, ibluey))

    while q:
        cnt, redx, redy, bluex, bluey = q.popleft()
        if cnt >= 10:
            return -1
        for di in range(4):
            next_redx, next_redy = redx, redy
            while True:
                if arr[next_redx][next_redy] == '#':
                    next_redx -= direction[di][0]
                    next_redy -= direction[di][1]
                    break
                if arr[next_redx][next_redy] == 'O':
                    break
                next_redx += direction[di][0]
                next_redy += direction[di][1]


            next_bluex, next_bluey = bluex, bluey
            while True:
                if arr[next_bluex][next_bluey] == '#':
                    next_bluex -= direction[di][0]
                    next_bluey -= direction[di][1]
                    break
                if arr[next_bluex][next_bluey] == 'O':
                    break
                next_bluex += direction[di][0]
                next_bluey += direction[di][1]

            # 구슬이 구멍에 빠졌다면
            if arr[next_bluex][next_bluey] == 'O':
                continue
            elif arr[next_redx][next_redy] == 'O':
                return cnt + 1

            # 만약 좌표가 같다면
            if next_redx == next_bluex and next_redy == next_bluey:
                dis_red = abs(next_redx - redx) + abs(next_redy - redy)
                dis_blue = abs(next_bluex - bluex) + abs(next_bluey - bluey)
                if dis_red > dis_blue:
                    next_redx -= direction[di][0]
                    next_redy -= direction[di][1]
                else:
                    next_bluex -= direction[di][0]
                    next_bluey -= direction[di][1]

            if next_redx != redx or next_redy != redy or next_bluex != bluex or next_bluey != bluey:
                q.append((cnt+1, next_redx, next_redy, next_bluex, next_bluey))
    return -1

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]


redx, redy = 0, 0
bluex, bluey = 0, 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'R':
            redx, redy= i, j
        elif arr[i][j] == 'B':
            bluex, bluey = i, j

direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]
answer = solve(0, redx, redy, bluex, bluey)
print(answer)

