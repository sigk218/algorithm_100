# https://www.acmicpc.net/problem/16235

import sys
sys.stdin = open('input.txt','r')

n, m, k = map(int, input().split())

# 양분
A = [list(map(int, input().split())) for _ in range(n)]


# 나무의 정보
trees = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, year = map(int, input().split())
    trees[x-1][y-1].append(year)

# 문제가 이해가 안됨. ㅜ -> 문제좀 똑바로 읽자.. !
# 가장 처음에 양분은 모든 칸에 5만큼
land = [[5 for _ in range(n)] for _ in range(n)]

for _ in range(k):

    # 봄 -> 양분을 먹을 수 있으면, 나이를 1살 더 먹는다
    # 같은 칸에 나무가 여러 개라면 나이가 적은 순 부터
    for i in range(n):
        for j in range(n):
            if trees[i][j]:
                trees[i][j].sort()
                live = []
                dead = 0
                for age in trees[i][j]:
                    if age <= land[i][j]:
                        land[i][j] -= age
                        live.append(age+1)
                    else:
                        # 여름
                        dead += (age // 2)
                trees[i][j] = live
                land[i][j] += dead

    # 가을
    for x in range(n):
        for y in range(n):
            for age in trees[x][y]:
                if age % 5 == 0:
                    for dx, dy in (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1):
                        xx = x + dx
                        yy = y + dy
                        if xx < 0 or xx >= n or yy < 0 or yy >= n: continue
                        trees[xx][yy].append(1)


    # 겨울
    for i in range(n):
        for j in range(n):
            land[i][j] += A[i][j]

    # print(live)

cnt = 0
for i in range(n):
    for j in range(n):
        cnt += len(trees[i][j])
print(cnt)

# 시간초과... 시간 복잡도 계산하기
# heapq는 iteration할 때 방식이 다른듯.. ?
