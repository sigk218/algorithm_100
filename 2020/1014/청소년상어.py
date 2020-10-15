import sys
sys.stdin = open('input.txt', 'r')


# 물고기는 빈칸으로 이동할 수 있다
def fish_move(sx, sy):
    # 한 칸을 이동할 수 있다.
    # 상어가 있는 칸은 못지나감...
    for i in range(1, 17):
        # 잡아먹힌 고기라면 넘어간다
        if not fish[i]:
            continue

        (x, y) = fish[i]
        temp_n, temp_d = arr[x][y]

        # 이동할 수 있는 지 체크
        temp_d -= 1
        for i in range(8):
            temp_d += 1
            temp_d %= 8
            xx = x + dire[temp_d][0]
            yy = y + dire[temp_d][1]
            if any([xx < 0, xx >= n, yy < 0, yy >= n]):
                xx, yy = x, y
                continue
            # 상어가 있는 칸이면 다음칸으로 넘어간다
            if all([xx == sx, yy == sy]):
                continue
            # 물고기가 있거나 비어있다면
            if arr[xx][yy] or arr[xx][yy] == []:
                break
        # 갈 수 있는 방향이 없다면
        else:
            xx, yy = x, y
            # print('이동하지 않았습니다.')
            continue

        # 서로 위치 바꿈
        if arr[xx][yy]:
            (next_n, next_d) = arr[xx][yy]
            fish[temp_n], fish[next_n] = fish[next_n], fish[temp_n]
            arr[xx][yy], arr[x][y] = [temp_n, temp_d], [next_n, next_d]
        else:
            fish[temp_n] = [xx, yy]
            arr[xx][yy] = [temp_n, temp_d]
            arr[x][y] = []


import copy
def shark_move(x, y, d, result, t):
    global answer, arr, fish

    fish_move(x, y)
    # 최대 4칸 이동할 수 있다
    xx, yy = x, y
    for i in range(4):
        # print(result, xx, yy, dire[d][0], dire[d][1])
        xx += dire[d][0]
        yy += dire[d][1]
        # 이동할 수 있는 칸이 없을 때 끝난다
        if any([xx < 0, xx >= n, yy < 0, yy >= n]):
            answer = max(result, answer)
            return
        # 물고기가 없는 칸으로는 이동할 수 없다의 의미... 지나갈 수 는 있음 ! ㅜㅜ
        # 와 이거 진짜 이해가 안된다.. ㅜㅜ
        if arr[xx][yy] == []:
            answer = max(result, answer)
            x, y = xx, yy
            continue

        temp_arr, temp_fish = copy.deepcopy(arr), copy.deepcopy(fish)
        (num, fish_d) = arr[xx][yy]

        # 물고기 먹기
        arr[xx][yy] = []
        fish[num] = []

        shark_move(xx, yy, fish_d, result+num, t+[num])
        # 복원
        arr, fish = temp_arr, temp_fish

n = 4
arr = [[] for _ in range(n)]
fish = [[] for _ in range(17)]
dire = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
for i in range(n):
    t = list(map(int, input().split()))
    for j in range(0, 2 * n, 2):
        (a, b) = t[j:j+2]
        arr[i].append([a, b-1])
        fish[a] = [i, j // 2]

num, direction = arr[0][0]
# (0, 0)의 물고기 잡아먹기
arr[0][0] = []
fish[num] = []
answer = 0
shark_move(0, 0, direction, num, [num])
print(answer)

# 으헝헝 ㅠㅠㅠ 진짜 왜이렇게 문제를 똑바로 안읽은거야 ㅠㅠ
# 갑자기 처음 보는 문제에 대해 자신 확 없어짐
# 1. 백트레킹 복원 (2차원 배열)
# 2. 물고기의 이동
# 3. 상어의 이동
# 동빈님 방법대로.. 풀어봐야지..
