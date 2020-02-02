import sys
sys.stdin = open('input.txt', 'r')

n, m, cx, cy, k = map(int, input().split())
totalmap = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(int, input().split()))

# 위쪽, 오른쪽, 왼쪽, 북쪽, 아래1, 아래2
cube = [0] * 6

cubeindex = [
    # 동, 서, 북, 남
    (2, 0, 5, 3, 4, 1),
    (1, 5, 0, 3, 4, 2),
    (4, 1, 2, 0, 5, 3),
    (3, 1, 2, 5, 0, 4),
]
# 동, 서, 북, 남
idx = 0
direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]


for command in commands:
    # print(cube)
    idx = command-1
    cx += direction[idx][0]
    cy += direction[idx][1]
    # print(cx, cy)
    # 나가지 않을 때만 주사위를 굴려줘야한다.
    if 0 <= cx < n and 0 <= cy < m:
        temp = cube[:]
        for i in range(6):
            cube[i] = temp[cubeindex[idx][i]]
        if totalmap[cx][cy]:
            cube[5] = totalmap[cx][cy]
            totalmap[cx][cy] = 0
        else:
            totalmap[cx][cy] = cube[5]
        print(cube[0])
    else:
        cx -= direction[idx][0]
        cy -= direction[idx][1]

            



