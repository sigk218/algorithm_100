import sys
sys.stdin = open('input.txt', 'r')

n = int(input())

people = [list(map(int, input().split())) for _ in range(n)]
total_num = sum(sum(people, []))


def seperate(x, y, d1, d2):

    # 5번 구역 경계선
    for i in range(d1+1):
        area[x+i][y-i] = 5
        area[x+d2+i][y+d2-i] = 5

    for i in range(d2+1):
        # print(x + i, y + i)
        # print(x + d1 + i, y - d1 + i)
        area[x+i][y+i] = 5
        area[x+d1+i][y-d1+i] = 5

    # 1번 선거구
    for i in range(x+d1):
        for j in range(y+1):
            if area[i][j] == 5:
                break
            area[i][j] += 1
            total[0] += people[i][j]

    # 3번 선거구
    for i in range(x+d1, n):
        for j in range(y-d1+d2):
            if area[i][j] == 5:
                break
            area[i][j] += 3
            total[2] += people[i][j]

    # 2번 선거구
    for i in range(x+d2+1):
        for j in range(n-1, y, -1):
            if area[i][j] == 5:
                break
            area[i][j] += 2
            total[1] += people[i][j]

    # 4번 선거구
    for i in range(x+d2+1, n):
        for j in range(n-1, y-d1+d2-1, -1):
            if area[i][j] == 5:
                break
            area[i][j] += 4
            total[3] += people[i][j]

    temp = sum(total)
    total[4] = total_num - temp
# seperate(2, 4, 2, 1)
# print(area)

answer = 10000000
for d1 in range(n):
    for d2 in range(n):
        for x in range(n):
            for y in range(n):
                if x < x + d1 + d2 < n and 0 <= y - d1 < y < y + d2 < n:
                    area = [[0] * n for _ in range(n)]
                    total = [0] * 5
                    seperate(x, y, d1, d2)

                    total.sort()
                    answer = min(total[4]-total[0], answer)
print(answer)