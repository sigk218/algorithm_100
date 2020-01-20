import sys
sys.stdin = open('input.txt', 'r')

def init():

    board[n//2-1][n//2-1] = 2
    board[n//2][n//2] = 2

    board[n//2-1][n//2] = 1
    board[n//2][n//2-1] = 1

def check(x, y, color):

    flip_list = []

    for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1):
        # 돌인데 나와 다른 색이라면 그 방향으로 계속 체크 해보기
        xx = x + dx
        yy = y + dy
        temp = []
        if 0 <= xx < n and 0 <= yy < n:
            if board[xx][yy] != color and board[xx][yy] != 0:
                while True:
                    temp.append((xx, yy))
                    xx += dx
                    yy += dy
                    if xx < 0 or xx >= n or yy < 0 or yy >= n:
                        break
                    if board[xx][yy] == 0:
                        break
                    if board[xx][yy] == color:
                        flip_list += temp
                        break
    return flip_list


T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    board = [[0] * n for _ in range(n)]
    init()

    for mm in range(m):
        #  흑돌 : 1 백돌 : 2
        x, y, color = map(int, input().split())
        x -= 1
        y -= 1
        board[x][y] = color
        temp = check(x, y, color)

        for r, c in temp:
            board[r][c] = color
            # pritn(board)

    wcnt, bcnt = 0, 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                bcnt += 1
            elif board[i][j] == 2:
                wcnt += 1
    print('#{} {} {}'.format(tc+1, bcnt, wcnt))

