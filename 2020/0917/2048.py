import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 블록 한줄을 이동시킨다(왼쪽으로 이동)
def play(line):

    result = []
    m = len(line)
    i = 0
    while i < m:
        if i+1 < m and line[i] == line[i+1]:
            result.append(line[i] + line[i+1])
            i += 2
        else:
            result.append(line[i])
            i += 1
    return result






# 블록을 방향 별로 돌려준다
def rotate(d, arr):
    result = [[0 for _ in range(n)] for _ in range(n)]
    # 위쪽일 때,
    if d == 0:
        for i in range(n):
            temp = []
            for j in range(n):
                if arr[j][n-1-i] == 0:continue
                temp.append(arr[j][n-1-i])
            line = play(temp)
            for j in range(len(line)):
                result[j][n-1-i] = line[j]
    # 아래 쪽일 때,
    elif d == 1:
        for i in range(n):
            temp = []
            for j in range(n):
                if arr[n-1-j][i] == 0:continue
                temp.append(arr[n-1-j][i])
            line = play(temp)

            for j in range(len(line)):
                result[n-1-j][i] = line[j]

    # 오른 쪽 일떄,
    elif d == 2:
        for i in range(n):
            temp = []
            for j in range(n):
                if arr[i][n-1-j] == 0: continue
                temp.append(arr[i][n-1-j])
            # print(temp)
            line = play(temp)
            # print(line)
            for j in range(len(line)):
                result[i][n-1-j] = line[j]

        pass
    # 왼쪽일 때,
    else:
        for i in range(n):
            temp = []
            for j in range(n):
                if arr[i][j] == 0:continue
                temp.append(arr[i][j])
            line = play(temp)
            for j in range(len(line)):
                result[i][j] = line[j]
    return result

import itertools

# 5번을 뽑는다 4 ** 5 = 1024 -> 줄세우기(순열)
# 위, 아래, 오른쪽, 왼쪽

answer = -1
for candidate in list(itertools.product([0, 1, 2, 3], repeat=5)):
    new_arr = arr
    for direction in candidate:
        new_arr = rotate(direction, new_arr)
        answer = max(answer, max(sum(new_arr, [])))
print(answer)