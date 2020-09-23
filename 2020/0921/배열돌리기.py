# https://www.acmicpc.net/problem/17406

# 회전 하기
def rotate(origin, r, c, s):
    # 새로운 배열 만들기
    result = [[0 for _ in range(m)] for _ in range(n)]

    # 새로운 배열에 원래 값 추가하기
    for i in range(n):
        for j in range(m):
            if (r-s-1 <= i < r+s) and (c-s-1 <= j < c+s):continue
            result[i][j] = origin[i][j]

    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    sx, sy = r-s-1, c-s-1
    x, y = r-s-1, c-s-1
    idx = 0
    while True:

        before = origin[x][y]

        # 넣을 곳을 찾기
        x += direction[idx][0]
        y += direction[idx][1]

        # 벽 바깥으로 나가면 방향을 바꾼다.
        if x < 0 or x >= n or y < 0 or y >= m or result[x][y]:
            x -= direction[idx][0]
            y -= direction[idx][1]
            idx += 1
            x += direction[idx][0]
            y += direction[idx][1]

        result[x][y] = before

        if x == sx and y == sy:
            if sx+1 == r-1 and sy+1 == c-1:
                result[sx+1][sy+1] = origin[sx+1][sy+1]
                return result
            sx += 1
            sy += 1
            x = sx
            y = sy
            idx = 0

import sys
sys.stdin = open('input.txt', 'r')


n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

command = []
for _ in range(k):
    r, c, s = map(int, input().split())
    command.append((r, c, s))

import itertools
# 뽑기 -> 순열로
answer = 5001
for candidate in list(itertools.permutations(command, k)):
    temp = arr
    for r, c, s in candidate:
        result = rotate(temp, r, c, s)
        temp = result
    # 최솟 값 찾기
    for i in range(n):
        answer = min(answer, sum(temp[i]))
print(answer)