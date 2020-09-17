import sys
sys.stdin = open('input.txt', 'r')

# 위 방향으로 올라가면서 오른쪽 왼쪽 체크
# 오/ 왼중 하나에서 1이 나온다면 0이 나올 때 까지 간다.
def inbox(x, y):
    if 0 <= x < 100 and 0 <= y < 100: return True
    else: return False

def go(x, y, direction):

    dy = -1
    if direction == 1:
        dy = 1

    # 1 : 오른쪽, 0 : 왼쪽
    while inbox(x, y) and ladder[x][y] == 1:
        y += dy
    return x, y-dy


T = 10
for tc in range(T):
    n = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    sx, sy = 99, ladder[99].index(2)

    while inbox(sx, sy) and sx > 1:

        sx -= 1

        # 오른 쪽 체크 하기
        if inbox(sx, sy+1) and ladder[sx][sy+1] == 1:
            sx, sy = go(sx, sy+1, 1)
        # 왼 쪽 체크 하기
        elif inbox(sx, sy-1) and ladder[sx][sy-1] == 1:
            sx, sy = go(sx, sy-1, 0)

    print('#{} {}'.format(tc+1, sy))

