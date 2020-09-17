import sys
sys.stdin = open('input.txt', 'r')

# 회전
#  U 윗면 D 아랫면 F 앞면 B 뒷면 L 왼쪽면 R 오른쪽면
# + 시계, - 반시계 (12개 이지만, 반시계를 시계 * 3으로 처리하면 빠르게 풀 수 있다.)

rotate_line = [
    [36, 37, 38, 18, 19, 20, 45, 46, 47, 27, 28, 29],
    [44, 43, 42, 35, 34, 33, 53, 52, 51, 26, 25, 24],
    [38, 41, 44, 9, 10, 11, 51, 48, 45, 8, 7, 6],
    [47, 50, 53, 17, 16, 15, 42, 39, 36, 0, 1, 2],
    [29, 32, 35, 15, 12, 9, 24, 21, 18, 6, 3, 0],
    [20, 23, 26, 11, 14, 17, 33, 30, 27, 2, 5, 8],
]


def rotate(side, direction):
    # 바깥 라인 바꿔주기
    for d in range(direction):
        new_line = [0] * 12
        for i in range(12):
            new_line[(i-3+12) % 12] = cube[rotate_line[side][i]]
        for i in range(12):
            cube[rotate_line[side][i]] = new_line[i]

        # 중간 판 돌려주기
        side_temp = [[0] * 3 for _ in range(3)]
        idx = 0
        for i in range(3):
            for j in range(3):
                side_temp[i][j] = cube[side*9+idx]
                idx += 1
        new_side = [[0] * 3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                new_side[j][i] = side_temp[3-1-i][j]
        # 값 넣어주기
        idx = 0
        for i in range(3):
            for j in range(3):
                cube[side*9+idx] = new_side[i][j]
                idx += 1

# 돌리기
sides = ['U', 'D', 'F', 'B', 'L', 'R']



n = int(input())
for tc in range(n):
    # 초기화
    cube = [''] * 54
    color = ['w', 'y', 'r', 'o', 'g', 'b']
    idx = 0
    for i in range(54):
        if i != 0 and i % 9 == 0: idx += 1
        cube[i] = color[idx]
    commands_len = int(input())
    commands = list(input().split())
    for command in commands:
        side = command[0]
        direction = command[1]
        if direction == '-' : direction = 3
        else: direction = 1
        rotate(sides.index(side), direction)
    idx = 1
    for i in range(3):
        print(''.join(cube[(idx-1)*3:idx*3]))
        idx += 1
    # print(cube)

