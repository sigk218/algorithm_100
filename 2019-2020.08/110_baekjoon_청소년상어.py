import sys
sys.stdin = open('input.txt', 'r')

# 물고기 방향과 상어의 방향이 바뀌는 지 고려 !

# 상어의 이동 (여러 칸)
# 상어가 먹을 수 있는 물고기 번호의 합의 최대 값
# 방향에 있는 칸으로 이동 o: 물고기가 있는 칸, 이동 x : 물고기가 없는 칸
# 이동할 수 있는 칸이 없으면 공간에서 벗어나 집으로
# 물고기가 있다 ? -> 그 칸에 물고기를 먹고 그 물고기의 방향을 가짐
# 이동하는 중에 지나가는 물고기는 먹지 x,

def inbox(x, y):
    if 0 <= x < 4 and 0 <= y < 4: return True

def change(i, nx, ny, x, y, new_board, new_fish):

    new_fish[new_board[nx][ny] - 1][1] = x
    new_fish[new_board[nx][ny] - 1][2] = y
    new_board[x][y] = new_board[nx][ny]

    new_fish[i][1] = nx
    new_fish[i][2] = ny
    new_board[nx][ny] = i + 1


# 물고기의 이동 (한 칸)
# 1. 번호가 작은 물고기 부터
# 2. 이동 o : 빈 칸, 다른 물고기가 있는 칸 -> 서로의 위치를 바꾼다
#  이동 x : 상어, 공간의 경계를 넘는 칸 -> 이동할 수 있을 때 까지 45도 반시계 회전 -> 그래도 없으면 이동 x

import copy

def move(ni, nj, fish, board):

    new_board = copy.deepcopy(board)
    new_fish = copy.deepcopy(fish)

    new_board[ni][nj] = 0
    for i in range(16):
        (d, x, y) = new_fish[i]
        if new_board[x][y] == 0:continue
        nx = x + dx[d]
        ny = y + dy[d]
        if inbox(nx, ny) and new_board[nx][ny]:
            # 위치를 바꾼다
            change(i, nx, ny, x, y, new_board, new_fish)
        else:
            # 이동할 수 있을 때 까지 반시계 회전
            for _ in range(8):
                d = (d + 1) % 8
                nx = x + dx[d]
                ny = y + dy[d]
                if inbox(nx, ny) and new_board[nx][ny]:
                    new_fish[new_board[x][y]-1][0] = d
                    change(i, nx, ny, x, y, new_board, new_fish)
                    break

    return new_fish, new_board

def solve(i, j, dir, fish, board, cnt):
    global visited, answer

    answer = max(cnt, answer)
    if not inbox(i+dx[dir], j+dy[dir]) or (inbox(i+dx[dir], j+dy[dir]) and board[i+dx[dir]][j+dy[dir]] == 0):
        return
    else:
        for it in range(1, 4):
            i += dx[dir]
            j += dy[dir]
            # ni = i + it * dx[dir]
            # nj = j + it * dy[dir]
            if not inbox(i, j): break
            if not visited[i][j]:
                visited[i][j] = 1
                temp = move(i, j, fish, board)
                solve(i, j, fish[board[i][j]-1][0], temp[0], temp[1], cnt+board[i][j])
                visited[i][j] = 0


dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

# 현재 있는 물고기 수
board = [[0 for _ in range(4)] for _ in range(4)]
# 좌표와 방향
fish = [0 for i in range(16)]

for i in range(4):
    temp = list(map(int, input().split()))
    for j in range(4):
        board[i][j] = temp[2*j]
        fish[temp[2*j]-1] = [temp[2*j+1]-1, i, j]



# move(fish, board)
visited = [[0 for _ in range(4)] for _ in range(4)]
answer = 0
first = board[0][0]
board[0][0] = 0
temp = move(0, 0, fish, board)
solve(0, 0, fish[first-1][0], temp[0], temp[1], first)
print(answer)
