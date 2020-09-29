import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

house = []
chicken = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            chicken.append((i, j))
        elif arr[i][j] == 1:
            house.append((i, j))
import itertools
# 치킨 중에 M 개를 뽑는다.
answer = 1000000
for candidate in list(itertools.combinations(chicken, m)):
    # 전체 치킨 거리
    total_dis = 0
    # 각 집의 치킨 거리
    for (i, j) in house:
        house_dis = 101
        # candidate 으로 해야하는데 chicken 으로 함 .. ㅠ
        for (x, y) in candidate:
            temp = abs(i-x) + abs(j-y)
            house_dis = min(house_dis, temp)
        total_dis += house_dis
    answer = min(total_dis, answer)

print(answer)





