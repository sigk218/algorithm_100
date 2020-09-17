import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
people = [list(map(int, input().split())) for _ in range(n)]


def seperate():
    for d1 in range(n):
        for d2 in range(n):
            for x in range(n):
                for y in range(n):
                    if x < x + d1 + d2 < n and 0 <= y-d1 < y < y + d2 < n:
                        border(x, y, d1, d2)

def border(x, y, d1, d2):
    global answer
    border_map = [[0] * n for _ in range(n)]
    area = [0] * 5
    # 갯수 만큼만 만들 수 있음.
    border_dict = {i : [n+1, -1] for i in range(n)}
    for dd1 in range(d1+1):
        border_dict[x+dd1][0] = min(border_dict[x+dd1][0], y - dd1)
        border_dict[x+dd1][1] = max(border_dict[x+dd1][1], y - dd1)

        border_dict[x + d2 + dd1][0] = min(border_dict[x + d2 + dd1][0], y+d2-dd1)
        border_dict[x + d2 + dd1][1] = max(border_dict[x + d2 + dd1][1], y+d2-dd1)

        # print('1', x + dd1, y - dd1)
        # print('4', x + d2 + dd1, y + d2 - dd1)
    for dd2 in range(d2+1):
        border_dict[x+dd2][0] = min(border_dict[x+dd2][0], y + dd2)
        border_dict[x+dd2][1] = max(border_dict[x+dd2][1], y + dd2)

        border_dict[x + d1 + dd2][0] = min(border_dict[x + d1 + dd2][0], y - d1 + dd2)
        border_dict[x + d1 + dd2][1] = max(border_dict[x + d1 + dd2][1], y - d1 + dd2)

    numFive = 0
    for i, v in border_dict.items():
        if v[0] == n+1: continue
        for j in range(v[0], v[1]+1):
            border_map[i][j] = 5
            area[4] += border_map[i][j]

    for i in range(x+d1):
        for j in range(y+1):
            if border_map[i][j] == 5:
                break
            border_map[i][j] = 1
            area[0] += people[i][j]

    for i in range(x+d2+1):
        for j in range(n-1, y, -1):
            if border_map[i][j] == 5:
                break
            border_map[i][j] = 2
            area[1] += people[i][j]

    for i in range(x+d1, n):
        for j in range(y-d1+d2):
            if border_map[i][j] == 5:
                break
            border_map[i][j] = 3
            area[2] += people[i][j]

    for i in range(x+d2+1, n):
        for j in range(n-1, y-d1+d2, -1):
            if border_map[i][j] == 5:
                break
            border_map[i][j] = 4
            area[3] += people[i][j]
    area.sort()
    temp = area[4] - area[0]
    print(temp)
    answer = min(answer, temp)
    print(border_map)




answer = 10000000
# seperate()
border(2, 4, 1, 2)
print(answer)
