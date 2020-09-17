import sys, collections
sys.stdin = open('input.txt', 'r')

# 뱀이 벽을 만나거나 자기 자신의 몸과 부딪히면 게임이 끝남
# 게임이 시작할 떄 뱀의 위치 (0, 0) 방향 오른쪽 길이 1

# 위, 오른쪽, 아래, 왼쪽
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

n = int(input())
board = [[0] * n for _ in range(n)]
# 1행 1열부터 시작
for k in range(int(input())):
    i, j = map(int, input().split())
    # 2는 사과
    board[i-1][j-1] = 2
# print(board)
commands = []
for l in range(int(input())):
    seconds, d = input().split()
    commands.append((int(seconds), d))

snake = collections.deque()
snake.append((0, 0))
snake_d = 1
board[0][0] = 1
time, idx = 0, 0
while True:

    snake_l = len(snake)
    b_x, b_y = snake[snake_l-1]
    # 머리를 한칸 앞으로
    h_x = b_x + direction[snake_d][0]
    h_y = b_y + direction[snake_d][1]

    # 만약 내 몸과 닿았거나 벽을 만났다면 게임 종료
    if h_x < 0 or h_x >= n or h_y < 0 or h_y >= n or board[h_x][h_y] == 1:
        # print('우와!끝났다')
        time += 1
        break

    # 사과가 있으면
    elif board[h_x][h_y] == 2:
        board[h_x][h_y] = 1

    # 사과가 없으면
    else:
        board[h_x][h_y] = 1
        t_x, t_y = snake.popleft()
        board[t_x][t_y] = 0

    snake.append((h_x, h_y))


    time += 1
    # 시간이 되면 뱀의 방향을 전환해준다.
    if idx >= len(commands): continue
    if commands[idx][0] == time:
        # 오른쪽으로 90도 방향 회전
        if commands[idx][1] == 'D':
            snake_d = (snake_d + 1) % 4
        else:
            snake_d = (snake_d - 1 + 4) % 4
        idx += 1

print(time)
