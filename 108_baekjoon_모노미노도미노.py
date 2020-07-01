# 연한 칸이 마지막
# 사라질 때만 분리 가능 하다
# A : 점수와 타일이 있는 개수

import sys
sys.stdin = open('input.txt', 'r')

# 움직이는거 -> 하나에 대해서만 -> 타입이랑, 색깔
# 좌표, 타입, 색
def move(cnt, t, x, y, color):
    if x + 1 >= 10 or y + 1 >= 10 : return
    if t == 1:
        if color == 'green':
            for xi in range(x+1, 10):
                if board[xi][y]:
                    board[xi - 1][y] = cnt
                    return xi - 1, y
            else:
                board[xi][y] = cnt
                return xi, y
        elif color == 'blue':
            for yi in range(y+1, 10):
                if board[x][yi]:
                    board[x][yi - 1] = cnt
                    return x, yi-1
            else:
                board[x][yi] = cnt
                return x, yi
    elif t == 2:
        if color == 'green':
            for xi in range(x+1, 10):
                if board[xi][y] or board[xi][y + 1]:
                    board[xi - 1][y] = cnt
                    board[xi - 1][y + 1] = cnt
                    return xi - 1, y
            else:
                board[xi][y] = cnt
                board[xi][y + 1] = cnt

        elif color == 'blue':
            for yi in range(y+1, 10):
                if board[x][yi]:
                    board[x][yi - 1] = cnt
                    board[x][yi - 2] = cnt
                    return x, yi-2
            else:
                board[x][yi - 1] = cnt
                board[x][yi] = cnt
                return x, yi - 1
    else:
        if color == 'green':
            for xi in range(x+1, 10):
                if board[xi][y]:
                    board[xi - 1][y] = cnt
                    board[xi - 2][y] = cnt
                    return xi - 2, y
            else:
                board[xi - 1][y] = cnt
                board[xi][y] = cnt
                return xi - 1, y
        elif color == 'blue':
            for yi in range(y+1, 10):
                if board[x][yi] or board[x + 1][yi]:
                    board[x][yi - 1] = cnt
                    board[x + 1][yi - 1] = cnt
                    return x, yi - 1
            else:
                board[x][yi] = cnt
                board[x + 1][yi] = cnt
                return x, yi

def check():
    global score
    # 초록색 -> 행이나 파란색 -> 열이 체크 될 경우
    change = []
    for i in range(4):
        rowsum = 0
        colsum = 0
        for j in range(4):
            if board[6+i][j]:
                rowsum += 1
            if board[j][6+i]:
                colsum += 1

        # 삭제 할 좌표를 다 넘겨주기
        for j in range(4):
            if rowsum == 4:
                score += 1
                change.append(('green', 6+i, j))
            if colsum == 4:
                score += 1
                change.append(('blue', j, 6+i))

    return change


board = [[0 for _ in range(10)] for _ in range(10)]


n = int(input())
green = []
blue = []
score = 0
for ni in range(n):
    t, x, y = map(int, input().split())
    green.append([t, move(ni+1, t, x, y, 'green')])
    blue.append([t, move(ni+1, t, x, y, 'blue')])
    # print(green, blue)
    # 체크하고 움직이고 체크하고 움직이는 과정 !
    while True:
        gflag = False
        bflag = False
        chklist = check()
        if not chklist: break
        if chklist:
            for (color, x, y) in chklist:
                idx = board[x][y]
                board[x][y] = 0
                if color == 'green':
                    gflag = True
                    if green[idx-1][0] < 0: continue
                    if green[idx-1][0] == 1:
                        green[idx-1][0] = -1
                    else:
                        if green[idx-1][1] == (x, y):
                            if green[idx - 1][0] == 2:
                                green[idx-1][1] = (x, y+1)
                            elif green[idx-1][0] == 3:
                                green[idx - 1][1] = (x+1, y)
                        green[idx-1][0] = 1

                if color == 'blue':
                    bflag = True
                    if blue[idx-1][0] < 0: continue
                    if blue[idx-1][0] == 1:
                        blue[idx-1][0] = -1
                    else:
                        if blue[idx-1][1] == (x, y):
                            if blue[idx - 1][0] == 2:
                                blue[idx-1][1] = (x, y+1)
                            elif blue[idx-1][0] == 3:
                                blue[idx - 1][1] = (x+1, y)
                        blue[idx-1][0] = 1
        # print('--------------')
        # print(*board, sep='\n')
        # print(gflag, green)
        # print(bflag, blue)
        # 초록, 파랑을 돌면서 블록들 이동하기
        if gflag:
            for type, (xi, yi) in green:
                if type == -1: continue
                idx = board[xi][yi] - 1
                green[idx] = [type, move(ni + 1, type, xi, yi, 'green')]
                # print('여기입니다', type, xi, yi, move(ni + 1, type, xi, yi, 'green'))
        if bflag:
            for type, (xi, yi) in blue:
                if type == -1: continue
                idx = board[xi][yi] - 1
                blue[idx] = [type, move(ni + 1, type, xi, yi, 'blue')]
                # print('여기입니다', type, xi, yi, move(ni + 1, type, xi, yi, 'blue'))

    # 연한 색 칸이 있을 때
    gcnt = 0
    bcnt = 0
    # print(*board, sep='\n')
    for i in range(4, 6):
        # 초록 색
        if sum(map(bool, board[i])) > 0:
            gcnt += 1
        # 파랑 색
        for j in range(4):
            if board[j][i]:
                bcnt += 1
                break
    # 녹색 옮기기

    # 파란색 옮기기
    print(gcnt, bcnt)





