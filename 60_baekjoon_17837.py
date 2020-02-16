import sys
sys.stdin = open('input.txt', 'r')


#  턴의 번호가  1000이상이거나 절대로 게임이 종료되지 않는 경우에는 -1
# 1. 1번부터 K번 까지 순서대로 말을 이동시키기
# 1-1. 한 말이 이동할 때 위에 올려져 있는 말도 함께 이동


# 오른쪽 , 왼쪽, 위, 아래
direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]

n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 순서대로 말의 현재 좌표
horses = [[] for _ in range(k)]
# 현재 보드 상황
horse_board = {(i, j): [] for i in range(n) for j in range(n)}

for kk in range(k):
    x, y, d = map(int, input().split())
    horses[kk] += [x-1, y-1, d-1]
    horse_board[(x-1, y-1)].append(kk)

turn = 0
flag = False
while True:
    for kk in range(k):
        # 만약 이전에 4개 이상의 말이 쌓여있다면 break
        if flag: break
        # print(horses)
        # print(horse_board)
        x, y, d = horses[kk]
        if len(horse_board[(x, y)]) >= 4:
            flag = True
            break
        nx = x + direction[d][0]
        ny = y + direction[d][1]
        # 벽이거나 파란색인 경우
        if not (0 <= nx < n and 0 <= ny < n) or board[nx][ny] == 2:
            # 방향을 바꿔주고
            if d == 0:
                d = 1
            elif d == 1:
                d = 0
            elif d == 2:
                d = 3
            else:
                d = 2
            # 한칸 이동한다
            nx = x + direction[d][0]
            ny = y + direction[d][1]
            # print(nx, ny, x, y, d)

        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 2:
            temp_idx = horse_board[(x, y)].index(kk)
            temp = horse_board[(x, y)][temp_idx:]
            horse_board[(x, y)] = horse_board[(x, y)][0:temp_idx]
            # 빨간색이면 뒤집어 준다
            if board[nx][ny] == 1:
                temp.reverse()
            # 보드에 합쳐준다.
            horse_board[(nx, ny)] += temp
            # 이동한 말들의 좌표를 바꿔준다.
            for t in temp:
                horses[t][0] = nx
                horses[t][1] = ny
            # 현재 나의 좌표를 바꿔준다.
            horses[kk] = [nx, ny, d]

        # 3. 한칸 이동한 칸이 파란색이거나 체스판을 벗어나는 경우
        else:
            # 방향만 반대로 바꾼다.
            nx, ny = x, y
            horses[kk] = [x, y, d]
        # 매턴마다 검사해준다.
        if len(horse_board[(nx, ny)]) >= 4:
            flag = True
            break

    turn += 1
    if flag:
        break
    if turn >= 1000:
        turn = -1
        break

print(turn)
