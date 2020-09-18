import sys
sys.stdin = open('input.txt', 'r')

n = int(input())

board = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(int(input())):
    i, j = map(int, input().split())
    # 사과는 8
    board[i-1][j-1] = 8

command = []
for _ in range(int(input())):
    s, v = input().split()
    command.append((int(s), v))


# 위, 오른, 아래, 왼
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
x, y, d = 0, 0, 1
second, idx = 0, 0
# 0 -> 꼬리, 끝 -> 머리
q = [(0, 0)]
while True:

    if idx < len(command) and second == command[idx][0]:
        if command[idx][1] == 'D':
            d = (d+1) % 4
        else:
            d = (d+3) % 4
        idx += 1

    xx = x + direction[d][0]
    yy = y + direction[d][1]

    if xx < 0 or xx >= n or yy < 0 or yy >= n:
        break
    if board[xx][yy] == 1:
        break

    if board[xx][yy] == 8:
        board[xx][yy] = 0
    elif board[xx][yy] == 0:
        # 이부분 틀렸었음 ! ! (꼬리로 안하고 이전 머리로함..!)
        i, j = q.pop(0)
        board[i][j] = 0

    # 몸 길이를 늘려 머리를 다음칸에 위치
    q.append((xx, yy))
    board[xx][yy] = 1

    x = xx
    y = yy
    second += 1


print(second+1)