import sys
sys.stdin = open('input.txt', 'r')
def wall(x, y):
    if 0 <= x < n and 0 <= y < n and answer[x][y] == 0:
        return False
    else:
        return True
T = int(input())
for tc in range(T):
    print('#{} '.format(tc+1))
    n = int(input())
    answer = [[0] * n for _ in range(n)]
    x, y = 0, 0
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    idx = 0
    number = 1

    while not wall(x, y):
        answer[x][y] = number
        number += 1
        x += direction[idx][0]
        y += direction[idx][1]

        if wall(x, y):
            x -= direction[idx][0]
            y -= direction[idx][1]
            idx = (idx+1) % 4
            x += direction[idx][0]
            y += direction[idx][1]

    for i in range(n):
        for j in range(n):
            print(answer[i][j], end=' ')
        print()