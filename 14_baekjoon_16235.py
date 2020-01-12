import sys
sys.stdin = open('input.txt', 'r')

from collections import deque
def springSummner():
    for (x, y), years in woods_dict.items():
        alive_wood = deque()
        temp = 0
        for year in years:
            if yangboon[x][y] >= year:
                alive_wood.append(year+1)
                yangboon[x][y] -= year
            else:
                temp += year // 2
        yangboon[x][y] += temp
        woods_dict[(x, y)] = alive_wood
def fall():
    # 몇 그루가 생길지만 알면 된다.
    for (x, y), years in woods_dict.items():
        for year in years:
            if year % 5 == 0:
                for dx, dy in (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1):
                    xx = x + dx
                    yy = y + dy
                    if 0 <= xx < n and 0 <= yy < n:
                        woods_dict[(xx, yy)].appendleft(1)

def winter():
    for i in range(n):
        for j in range(n):
            yangboon[i][j] += A[i][j]
n, m, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
yangboon = [[5] * n for _ in range(n)]
woods_dict = {(i, j): deque() for i in range(n) for j in range(n)} # 이런 것도 가능하다!
# 입력으로 주어지는 나무의 위차는 모두 서로 다르다.
# 좌표는 1,1 부터 시작
# 나무가 먹는 양분은 별로 중요하지 않다.
for mm in range(m):
    x, y, year = map(int, input().split())
    woods_dict[(x-1, y-1)].append(year)
for kk in range(k):
    springSummner()
    fall()
    winter()
cnt = 0
for _, year in woods_dict.items():
    cnt += len(year)
print(cnt)