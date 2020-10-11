import sys
sys.stdin = open('input.txt', 'r')

def rotate(nth, d, k):
    # d방향으로 k칸
    # 0 : 시계, 1: 반시계
    new_line = [0 for _ in range(m)]

    if d == 1:
        for i in range(m):
            new_line[i] = arr[nth][(i+k) % m]
    else:
        for i in range(m):
            new_line[i] = arr[nth][(i-k+m) % m]
    return new_line


import collections
def remove(xi, yi, visited):
    global t

    stack = collections.deque()
    stack.append((xi, yi))

    while stack:
        x, y = stack.pop()
        for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
            xx = x + dx
            yy = (y + dy + m) % m
            if xx < 0 or xx >= n:continue
            if visited[xx][yy]:continue
            if arr[x][y] == arr[xx][yy]:
                visited[xx][yy] = 1
                t.append((xx, yy))
                stack.append((xx, yy))

def get_avg():
    total, cnt = 0, 0

    for i in range(n):
        for j in range(m):
            if arr[i][j] <= 0: continue
            total += arr[i][j]
            cnt += 1

    # 원판에 숫자가 남아있지 않다면
    if cnt == 0:
        return

    # 평균 보다 작은 수는 +1, 큰수는 -1
    # avg = total / cnt

    for i in range(n):
        for j in range(m):
            if arr[i][j] == -1: continue
            if arr[i][j] * cnt > total:
                arr[i][j] -= 1
            elif arr[i][j] * cnt < total:
                arr[i][j] += 1


n, m, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

for _ in range(T):
    x, d, k = map(int, input().split())

    for idx in range(n):
        if (idx + 1) % x: continue
        arr[idx] = rotate(idx, d, k)
    # print(*arr, sep='\n')

    removed = False
    visited = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j] == -1 or visited[i][j]: continue
            t = [(i, j)]
            visited[i][j] = 1
            remove(i, j, visited)
            if len(t) > 1:
                removed = True
                for nx, ny in t:
                    arr[nx][ny] = -1

    # 인접하면서 수가 같은 것이 없다면
    if not removed:
        get_avg()

    # print()
    # print(*arr, sep='\n')

# 정답 구하기
answer = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == -1:continue
        answer += arr[i][j]
print(answer)

# 이것을 왜 그땐,... 못풀었을까..
# 원판에서 dfs 돌리는게 힘든듯 !
# 그놈의 런타임에러! ㅜㅜ ... 범위아니면 나누기인데.. 못찾겠다.. ㅜㅜ
# 재귀 호출이 너무 깊어져서 런타임 에러가 난듯..
# dfs 한 번에 돌리면 더 빠르다
# https://rbehd001.tistory.com/10