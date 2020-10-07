import sys
sys.stdin = open('input.txt', 'r')


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

blank = []
virus = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            blank.append((i, j))
        elif arr[i][j] == 2:
            virus.append((i, j))


# 벽을 세울 빈 칸을 세개 뽑는다
answer = -1
import itertools, collections
for candidate in list(itertools.combinations(blank, 3)):
    for x, y in candidate:
        arr[x][y] = 1

    change = []
    # 바이러스를 퍼뜨린다
    q = collections.deque(virus)
    while q:
        xi, yi = q.popleft()
        for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
            xx = xi + dx
            yy = yi + dy
            if xx < 0 or xx >= n or yy < 0 or yy >= m:continue
            if arr[xx][yy]: continue
            arr[xx][yy] = 2
            change.append((xx, yy))
            q.append((xx, yy))

    safe_area = 0
    # 안전 영역의 갯수를 센다
    for x in range(n):
        for y in range(m):
            if arr[x][y] == 0:
                safe_area += 1

    answer = max(answer, safe_area)

    # 복원 한다
    for x, y in change:
        arr[x][y] = 0
    for x, y in candidate:
        arr[x][y] = 0

print(answer)

# 분명히 로컬에서 돌릴때는 시간이 안 될것같은데.. ㅋㅋㅋ