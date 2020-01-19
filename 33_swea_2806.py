import sys
sys.stdin = open('input.txt', 'r')


def inbox(x, y):
    if 0 <= x < n and 0 <= y < n: return True
    else: return False

def ispossible(x, y):

    for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1):
        xx, yy = x, y
        while inbox(xx, yy):
            xx += dx
            yy += dy
            # 해당 줄을 다 검사 해 봤을 때
            if inbox(xx, yy) and visited[xx][yy] != 0:
                return False
    return True



def NQueen(d):
    global cnt

    if d == n:
        cnt += 1
    else:
        for i in range(n):
            # 방문하지 않고, 8방향으로도 놓인게 없어야함
            if not visited[d][i] and ispossible(d, i):
                visited[d][i] = 1
                NQueen(d+1)
                visited[d][i] = 0


T = int(input())
for tc in range(T):
    n = int(input())

    visited = [[0] * n for _ in range(n)]
    cnt = 0
    NQueen(0)
    print('#{} {}'.format(tc+1, cnt))