import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]

empty = []
virus = []
for nn in range(n):
    for mm in range(m):
        if li[nn][mm] == 0:
            empty.append((nn, mm))
        elif li[nn][mm] == 2:
            virus.append((nn, mm))
def check():
    cnt = 0
    for nn in range(n):
        for mm in range(m):
            if li[nn][mm] == 0:
                cnt += 1
    return cnt

def wall(x, s):
    global answer
    if x == 3:
        for x, y in t:
            li[x][y] = 1
        change_list = []
        spread(change_list)
        # print(check())
        answer = max(answer, check())
        for x, y in t:
            li[x][y] = 0
        clean(change_list)

    else:
        for i in range(s, num_empty):
            if not visited[i]:
                visited[i] = 1
                t.append((empty[i][0], empty[i][1]))
                wall(x+1, i)
                t.pop()
                visited[i] = 0


def spread(change_list):
    visited = [[0] * m for _ in range(n)]
    for i, j in virus:
        if not visited[i][j]:
            q = []
            q.append((i, j))
            visited[i][j] = 1

            while q:
                x, y = q.pop(0)
                for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                    xx = x + dx
                    yy = y + dy
                    if 0 <= xx < n and 0 <= yy < m and not visited[xx][yy]:
                        if li[xx][yy] == 0:
                            li[xx][yy] = 2
                            visited[xx][yy] = 1
                            q.append((xx, yy))
                            change_list.append((xx, yy))

def clean(change_list):
    for x, y in change_list:
        li[x][y] = 0

num_empty = len(empty)

visited = [0] * num_empty
answer = 0
t = []
wall(0, 0)
print(answer)

