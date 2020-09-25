# https://www.acmicpc.net/problem/14499

import sys
sys.stdin = open('input.txt', 'r')

n, m, x, y, k = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(int, input().split()))

# 1 ~ 6
dice = [0 for _ in range(7)]

# 방향에 따른 주사위 변화
change = {
    # 동
    1: [4, 2, 1, 6, 5, 3],
    # 서
    2: [3, 2, 6, 1, 5, 4],
    # 북
    3: [5, 1, 3, 4, 6, 2],
    # 남
    4: [2, 6, 3, 4, 1, 5],
}

direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]

for command in commands:
    # print(command)

    nx = x + direction[command-1][0]
    ny = y + direction[command-1][1]
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
    # print(dice)
    new_dice = [0 for _ in range(7)]
    for i in range(1, 7):
        idx = change[command][i-1]
        new_dice[i] = dice[idx]
    if arr[nx][ny] == 0:
        # 주사위의 바닥 면에 쓰여 있는 수가 칸에 복사
        arr[nx][ny] = new_dice[6]
    else:
        # 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사
        new_dice[6] = arr[nx][ny]
        arr[nx][ny] = 0
    dice = new_dice
    x, y = nx, ny
    # print(dice)
    print(dice[1])
