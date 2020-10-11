import sys
sys.stdin = open('input.txt', 'r')


def find_shop(x, y, k1, k2):

    total = []
    total.append(arr[x][y])

    for kk1 in range(1, k1+1):
        total.append(arr[x + kk1][y - kk1])
        total.append(arr[x + k2 + kk1][y + k2 - kk1])


    for kk2 in range(1, k2+1):
        total.append(arr[x + kk2][y + kk2])
        total.append(arr[x + k1 + kk2][y - k1 + kk2])

    total.pop()
    return len(total) if len(set(total)) == len(total) else -1



T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    answer = -1
    for sx in range(0, n-1):
        for sy in range(1, n-1):
            for k1 in range(1, n):
                for k2 in range(1, n):
                    if any([sx + k1 + k2 >= n, sy-k1 < 0, sy + k2 >= n]):continue
                    t = find_shop(sx, sy, k1, k2)
                    answer = max(answer, t)
    print('#{} {}'.format(tc, answer))
