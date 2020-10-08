import sys
sys.stdin = open('input.txt', 'r')


def move(arr, t, x, y):
    # 다른 블록을 만나거나 보드의 경계를 만나기 전 까지
    arr[x][y] = 0
    if t == 1:
        while True:
            if x > 5:
                x -= 1
                break
            elif arr[x][y]:
                x -= 1
                break
            x += 1
        arr[x][y] = t
        return

    elif t == 2:
        arr[x][y+1] = 0
        while True:
            if x > 5:
                x -= 1
                break
            elif arr[x][y] or arr[x][y+1]:
                x -= 1
                break
            x += 1
        arr[x][y] = t
        arr[x][y+1] = 8
        return

    else:
        arr[x+1][y] = 0
        x += 1
        while True:
            if x > 5:
                x -= 1
                break
            elif arr[x][y]:
                x -= 1
                break
            x += 1
        arr[x-1][y] = t
        arr[x][y] = 9
        return

def remove(arr):

    score = 0
    for i in range(6):
        # 한 행이 가득찻는지 체크
        if sum(list(bool(arr[i][j]) for j in range(4))) != 4:
            continue
        score += 1
        for j in range(4):
            # 연결 되어 있던 거라면 끊어 줘야 한다
            if arr[i][j] == 1:
                arr[i][j] = 0
            elif arr[i][j] == 2:
                arr[i][j] = 0
                arr[i][j+1] = 0
            elif arr[i][j] == 8:
                arr[i][j] = 0
                arr[i][j-1] = 0
            elif arr[i][j] == 3:
                arr[i][j] = 0
                arr[i+1][j] = 1
            elif arr[i][j] == 9:
                arr[i][j] = 0
                arr[i-1][j] = 1
        return score
    return score

def popline(arr):

    # 몇 행을 이동해야할 지
    cnt = 0
    for i in range(0, 2):
        if sum(arr[i]) > 0:
            cnt += 1

    if cnt == 0:
        return False, arr

    # 아래칸 지울 때, 타일 바꿔주기
    for i in range(6-1, 6-cnt-1, -1):
        for j in range(4):
            if arr[i][j] == 3:
                arr[i + 1][j] = 1
            elif arr[i][j] == 9:
                arr[i - 1][j] = 1

    return True, [[0 for _ in range(4)] for _ in range(cnt)] + arr[0:6-cnt]

green = [[0 for _ in range(4)] for _ in range(6)]
blue = [[0 for _ in range(4)] for _ in range(6)]

answer = 0
for _ in range(int(input())):

    t, x, y = map(int, input().split())


    # green
    # 1. 블록이 이동한다
    move(green, t, 0, y)
    # 2. 행이 가득찬 경우 0으로 표시 -> 이동
    while True:
        temp_score = remove(green)
        if temp_score == 0:
            break
        answer += temp_score
        # 더이상 지울 행이 없을 때까지 지운다
        for i in range(5, -1, -1):
            for j in range(4):
                if 1 <= green[i][j] <= 3:
                    move(green, green[i][j], i, j)




    # 3. 연한 칸 블록처리 -> 이동
    (ispop, green) = popline(green)
    # 연한 칸에 블록이 있었을 때만 이동하기
    if ispop:
        for i in range(6):
            for j in range(4):
                if 1 <= green[i][j] <= 3:
                    move(green, green[i][j], i, j)


    if t == 2:
        t = 3
    elif t == 3:
        t = 2


    # blue
    # 1. 최초 블록 이동
    move(blue, t, 0, x)

    # 2. 행이 가득찬 경우 0으로 표시 -> 이동
    while True:
        temp_score = remove(blue)
        if temp_score == 0:
            break
        answer += temp_score
        # 더이상 지울 행이 없을 때까지 지운다
        for i in range(5, -1, -1):
            for j in range(4):
                if 1 <= blue[i][j] <= 3:
                    move(blue, blue[i][j], i, j)

    # 3.연한 칸 블록처리 -> 이동
    (ispop, blue) = popline(blue)
    if ispop:
        for i in range(6):
            for j in range(4):
                if 1 <= blue[i][j] <= 3:
                    move(blue, blue[i][j], i, j)

cnt = 0
for i in range(6):
    for j in range(4):
        if green[i][j]:
            cnt += 1
        if blue[i][j]:
            cnt += 1
print(answer)
print(cnt)



'''
green = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [2, 8, 0, 0],
    [1, 0, 0, 3],
    [2, 8, 0, 9],
    [0, 1, 1, 1]
]

t, x, y = 2, 0, 2

'''





# 지우고 마지막으로 움직여줘야함!
# while 문 빠져나올 때 분기
# 아래서 부터 떨어져야함 -> 내가 이전에 떨어지는 문제를 푼 적이 없나.. ?
# 떨어질 때는 2번 모양은 고려할 필요가 없다.
