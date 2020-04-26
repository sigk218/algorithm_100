import sys, copy
sys.stdin = open('input.txt', 'r')

# 바이러스가 퍼질 수 없는 곳
def spread():
    # 내가 바꾼 바이러스
    result = []
    for i, j in virus:
        q = [(i, j)]
        t = []
        while q:
            x, y = q.pop(0)
            for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                xx = x + dx
                yy = y + dy
                if 0 <= xx < n and 0 <= yy < m and arr[xx][yy] == 0:
                    t.append((xx, yy))
                    arr[xx][yy] = 2
                    q.append((xx, yy))

        result += t
    b = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                b+= 1

    # print(result)
    return result, b


# 빈칸의 갯수를 센다
# 바이러스가 퍼진 곳을 뺀다
# 장애물이 없을 때 까지 퍼져나간다
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
blanks = 0
virus = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            blanks += 1
        elif arr[i][j] == 2:
            virus.append((i, j))


def choice(cnt, sx, sy):
    global answer
    if cnt == 3:
        # print('다 뽑았음')
        (change, now_b) = spread()
        for x, y in change:
            arr[x][y] = 0
        answer = max(answer, now_b)
        return
    else:
        for i in range(sx, n):
            ny = sy if i == sx else 0
            for j in range(ny, m):
                if arr[i][j] == 0:
                    arr[i][j] = 1
                    choice(cnt+1, i, j)
                    arr[i][j] = 0

answer = -1
choice(0, 0, 0)
print(answer)