# import sys
# sys.stdin = open('input.txt', 'r')

r, c, m = map(int, input().split())
shark = list(list([] for __ in range(c)) for _ in range(r))

# 위, 아래, 오른쪽, 왼쪽
direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def change(d):
    if d == 0:
        return 1
    elif d == 1:
        return 0
    elif d == 2:
        return 3
    elif d == 3:
        return 2

shark_list = dict()
for _ in range(m):
    rr, cc, s, d, z = map(int, input().split())
    # 크기, 속력, 이동방향
    shark[rr-1][cc-1].append([z, s, d-1])
    shark_list[(rr-1, cc-1)] = [z, s, d-1]


total = 0
# 1. 낚시왕 이동
for second in range(c):
    # 2. 해당 열의 상어 잡기 (가장 행의 번호가 낮은 순서)
    # print('--------------')
    # print(*shark, sep='\n')
    for i in range(r):
        if shark[i][second]:
            zz, ss, dd = shark[i][second].pop()
            total += zz
            del shark_list[(i, second)]
            break
    # 3. 상어 이동
    new_shark_list = dict()
    # 3-1. 칸 / 초 만큼 이동
    for (x, y), (z, s, d) in shark_list.items():
        shark[x][y] = []
        # 상에가 벽에 갔다가 원래 위치로 돌아오는데 걸리는 시간
        xx, yy, d = x, y, d
        temp_s = s % (((2 * r * abs(direction[d][0])) + (2 * c * abs(direction[d][1]))) - 2)
        for sss in range(temp_s):
            # 3-2. 격자판을 벗어나면 방향을 반대로 바꾼다. -> 방향을 바꿔 이동
            xx += direction[d][0]
            yy += direction[d][1]
            if not(0 <= xx < r and 0 <= yy < c):
                xx -= direction[d][0]
                yy -= direction[d][1]
                d = change(d)
                xx += direction[d][0]
                yy += direction[d][1]

        # 이미 있으면 비교해서 크기가 큰 것을 넣어준다.
        if new_shark_list.get((xx, yy)):
            tempz, _, __= new_shark_list[(xx, yy)]
            if tempz < z:
                new_shark_list[(xx, yy)] = [z, s, d]
        # 칸에 아무것도 없다면 그냥 넣어준다
        else:
            new_shark_list[(xx, yy)] = [z, s, d]
    shark_list = new_shark_list
    for (x, y), (z, s, d) in new_shark_list.items():
        shark[x][y].append([z, s, d])
print(total)





