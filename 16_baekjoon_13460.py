import sys
sys.stdin = open('input.txt', 'r')
# https://rebas.kr/724?category=766915
import collections

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
# red x, red y, blue x, blue y
balls = collections.deque()
visited = [[[0] * 4 for _ in range(n)] for _ in range(n)]
hx, hy = 0, 0


for nn in range(n):
    for mm in range(m):
        if board[nn][mm] == 'R':
            balls.appendleft((nn, mm))
        elif board[nn][mm] == 'B':
            balls.append((nn, mm))
        elif board[nn][mm] == 'O':
            hx, hy = nn, mm
print(balls, hx, hy)


def move(x, y, dx, dy):

    ax, ay = 0, 0

    while




def solve():

    bx, by = balls.pop()
    rx, ry = balls.pop()
    # 방문 체크

    for (dx, dy) in (0, 1), (1, 0), (0, -1), (-1, 0):
        # 해당 방향으로 움직였을때 최대로 멀리 간 값을 반환
