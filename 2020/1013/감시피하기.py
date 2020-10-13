import sys
sys.stdin = open('input.txt', 'r')

# 선생님 T, 학생 S, 장애물 O
# 감시 : 상, 하, 좌, 우
# 정확히 3개의 장애물을 설치 -> 모든 학생들이 감시를 피할 수 있는지 ?
def check(t):

    for x, y in t:
        for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
            xx = x
            yy = y
            while True:
                xx += dx
                yy += dy
                if any([xx < 0, xx >= n, yy < 0, yy >= n]):
                    break
                if arr[xx][yy] == 'S':
                    return False
                if arr[xx][yy] == 'O' or arr[xx][yy] == 'T':
                    break

    return True




n = int(input())
arr = [list(input().split()) for _ in range(n)]

t = []
blank = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'X':
            blank.append((i, j))
        elif arr[i][j] == 'T':
            t.append((i, j))

import itertools
for candidate in list(itertools.combinations(blank, 3)):
    for x, y in candidate:
        arr[x][y] = 'O'

    # 선생님이 4방향으로 가다가 학생을 만나면 실패
    if check(t):
        print("YES")
        exit()
    
    for x, y in candidate:
        arr[x][y] = 'X'
print('NO')