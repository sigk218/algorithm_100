import sys
sys.stdin = open('input.txt', 'r')


def make_road(x, y, d, check):
    global answer

    answer = max(d, answer)

    for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
        xx = x + dx
        yy = y + dy
        if any([xx < 0, xx >= n, yy < 0, yy >= n]):
            continue
        if visited[xx][yy]:
            continue
        if arr[xx][yy] < arr[x][y]:
            visited[xx][yy] = 1
            make_road(xx, yy, d+1, check)
            visited[xx][yy] = 0
            continue
        # 같거나 클 때
        if check:
            continue
        if abs(arr[xx][yy] - arr[x][y]) + 1 > k:
            continue
        if arr[x][y] - 1 < 0:
            continue
        temp = arr[xx][yy]
        arr[xx][yy] = arr[x][y] - 1
        visited[xx][yy] = 1
        make_road(xx, yy, d+1, check+1)
        arr[xx][yy] = temp
        visited[xx][yy] = 0






t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    max_points = []
    high = max(sum(arr, []))
    for i in range(n):
        for j in range(n):
            if arr[i][j] == high:
                max_points.append((i, j))

    answer = 0
    # print(max_points)
    for x, y in max_points:
        visited = [[0 for _ in range(n)] for _ in range(n)]
        visited[x][y] = 1
        make_road(x, y, 1, 0)
    print('#{} {}'.format(tc, answer))


# visited 하는거.. 욀케 못훼.. ? 들어가기 전에 체크하자 항상!
# 391ms