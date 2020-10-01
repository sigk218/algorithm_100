import sys
sys.stdin = open('input.txt', 'r')

# 돌려야할 옆면 3칸씩, -3 + 12 % 3
side = {
    'U': [36, 37, 38, 18, 19, 20, 45, 46, 47, 27, 28, 29],
    'D': [44, 43, 42, 35, 34, 33, 53, 52, 51, 26, 25, 24],
    'F': [38, 41, 44, 9, 10, 11, 51, 48, 45, 8, 7, 6],
    'B': [47, 50, 53, 17, 16, 15, 42, 39, 36, 0, 1, 2],
    'L': [29, 32, 35, 15, 12, 9, 24, 21, 18, 6, 3, 0],
    'R': [20, 23, 26, 11, 14, 17, 33, 30, 27, 2, 5, 8],
}


n = int(input())


for _ in range(n):
    # 큐브 초기 설정
    cube = ['' for i in range(54)]
    color = ['w', 'y', 'r', 'o', 'g', 'b']

    idx = 1
    for i in range(54):
        if i == idx * 9: idx += 1
        cube[i] = color[idx - 1]

    direction = ['U', 'D', 'F', 'B', 'L', 'R']

    command_len = int(input())
    command = list(input().split())
    for a in command:
        it = 1
        # 반 시계는 시계 * 3
        if a[1] == '-':
            it = 3
        for _ in range(it):
            # 바깥 라인 바꿔 주기
            new_line = [0] * 12
            # 시계 방향
            # print(cube[18:27])
            for i in range(12):
                # 여기서 모듈러 연산 ! -> 문제 완벽히 이해하기!
                # 주사위 모양 헷갈림
                new_line[i] = cube[side[a[0]][(i+3)%12]]
            for i in range(12):
                cube[side[a[0]][i]] = new_line[i]

            order = direction.index(a[0])

            temp_side = [[0] * 3 for _ in range(3)]
            idx = 0
            for i in range(3):
                for j in range(3):
                    temp_side[i][j] = cube[order*9+idx]
                    idx += 1
            new_side = [[0] * 3 for _ in range(3)]
            # 판 돌려주기
            for i in range(3):
                for j in range(3):
                    new_side[i][j] = temp_side[3-1-j][i]

            # 값 넣어주기
            idx = 0
            for i in range(3):
                for j in range(3):
                    cube[order*9+idx] = new_side[i][j]
                    idx += 1

    for i in range(0, 8, 3):
        print(''.join(cube[i:i+3]))
        idx += 3


# 너무 어려워서... 이전에 풀었던 것을 보고 다시 풀었습니다... 
# 꼭 다시 풀어봐야할 듯! -> 판, 옆 나눠서 생각하는 것, 시계 * 3 -> 반시계
# 넘버링을 잘못함 *^^*