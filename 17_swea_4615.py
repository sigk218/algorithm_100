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

    wcnt, bcnt = 0, 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                bcnt += 1
            elif board[i][j] == 2:
                wcnt += 1
    print('#{} {} {}'.format(tc+1, bcnt, wcnt))

# x, y = 3, 0
# board = [[2, 2, 2, 2], [1, 1, 1, 2], [0, 1, 2, 2], [2, 2, 2, 2]]

# delta = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, -1), (-1, 1), (1, 1), (-1, -1)]
# def inside(x, y):
#     return 0 <= x < N and 0 <= y < N
# TC = int(input())
# for tc in range(1, TC + 1):
#     N, M = map(int, input().split())
#     # 흑돌 1, 백돌 2
#     board = [[0] * N for _ in range(N)]
#     # print(*board, sep="\n")
#     n = N // 2
#     board[n - 1][n - 1] = board[n][n] = 2
#     board[n][n - 1] = board[n - 1][n] = 1
#     # print(*board, sep="\n")
#     for m in range(M):
#         # print(m, "번째")
#         Y, X, color = map(int, input().split())
#         x = X - 1
#         y = Y - 1
#         board[x][y] = color
#         for d in range(8):
#             dx = delta[d][0]
#             dy = delta[d][1]
#             # for n in range(N-1, 1, -1): # 뒤에서부터 해봄
#             for n in range(2, N):
#                 big_flag = False
#                 if inside(x + n * dx, y + n * dy) and board[x + n * dx][y + n * dy] == color:
#                     flag = True
#                     for bet in range(1, n):
#                         if board[x + bet * dx][y + bet * dy] != 3 - color:
#                             flag = False
#                     if flag == True:
#                         big_flag = True
#                         for bet in range(1, n):
#                             board[x + bet * dx][y + bet * dy] = color
#                 if big_flag == True:
#                     break
#     temp = sum(board, [])
#     print('#%d %d %d' % (tc, temp.count(1), temp.count(2)))