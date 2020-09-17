import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


def seperate(x, y, d1, d2):
    global people
    number = [[0 for _ in range(n)] for _ in range(n)]
    total = [0 for _ in range(5)]
    number[x][y] = 5
    for dx in range(1, d1+1):
        number[x+dx][y-dx] = 5
        number[x+d2+dx][y+d2-dx] = 5

    for dy in range(1, d2+1):
        number[x+d1+dy][y-d1+dy] = 5
        number[x+dy][y+dy] = 5

    # 1번 선거구
    for i in range(x+d1):
        for j in range(y+1):
            if number[i][j] == 5:
                break
            number[i][j] = 1
            total[0] += arr[i][j]
    # 2번 선거구
    for i in range(x+d2+1):
        for j in range(n-1, y, -1):
            if number[i][j] == 5:
                break
            number[i][j] = 2
            total[1] += arr[i][j]
    # 3번 선거구
    for i in range(x+d1, n):
        for j in range(y-d1+d2):
            if number[i][j] == 5:
                break
            number[i][j] = 3
            total[2] += arr[i][j]
    # 4번 선거구
    for i in range(x+d2+1, n):
        for j in range(n-1, y-d1+d2-1, -1):
            if number[i][j] == 5:
                break
            number[i][j] = 4
            total[3] += arr[i][j]
    total[4] = people - sum(total)
    total.sort()
    return total[4] - total[0]


people = sum(sum(arr, []))
answer = -1
for d1 in range(1, n):
    for d2 in range(1, n):
        for x in range(n):
            for y in range(n):
                if x+d1+d2 >= n or y-d1 < 0 or y+d2 >= n:continue
                if answer == -1: answer = seperate(x, y, d1, d2)
                else:
                    answer = min(answer, seperate(x, y, d1, d2))
print(answer)

