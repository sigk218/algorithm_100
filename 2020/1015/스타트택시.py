import sys
sys.stdin = open('input.txt', 'r')
import collections
def find_dis(xi, yi):

    q = collections.deque()
    distance = [[-1 for _ in range(n)] for _ in range(n)]
    distance[xi][yi] = 1
    q.append((xi, yi, 1))

    while q:
        x, y, d = q.popleft()
        for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
            xx = x + dx
            yy = y + dy
            if any([xx < 0, xx >= n, yy < 0, yy >= n]):
                continue
            # 방문 했거나 벽이면 계산할 필요 x
            if distance[xx][yy] != -1 or arr[xx][yy]:
                continue
            distance[xx][yy] = d + 1
            q.append((xx, yy, d+1))
    return distance

def find_passenger(dis):
    temp_dis, temp_x, temp_y, num = -1, 0, 0, -1

    for i in range(m):
        if start[i] == 0:
            continue
        if dis[start[i][0]][start[i][1]] == -1:
            continue
        if temp_dis == -1:
            temp_dis = dis[start[i][0]][start[i][1]]
            temp_x, temp_y = start[i][0], start[i][1]
            num = i
            continue
        if temp_dis > dis[start[i][0]][start[i][1]]:
            temp_dis = dis[start[i][0]][start[i][1]]
            temp_x, temp_y = start[i][0], start[i][1]
            num = i
        elif temp_dis == dis[start[i][0]][start[i][1]]:
            # 행 번호가 더 작은 것을 택한다
            if temp_x > start[i][0]:
                temp_x, temp_y = start[i][0], start[i][1]
                num = i
            # 행 번호도 같다면, 열 번호로 비교
            if temp_x == start[i][0] and temp_y > start[i][1]:
                temp_x, temp_y = start[i][0], start[i][1]
                num = i
    return temp_dis, temp_x, temp_y, num

def go_destination(sx, sy, ex, ey):

    q = collections.deque()
    distance = [[0 for _ in range(n)] for _ in range(n)]
    distance[sx][sy] = 1
    q.append((sx, sy, 1))

    while q:
        x, y, d = q.popleft()
        if x == ex and y == ey:
            return True, distance[x][y] - 1
        for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
            xx = x + dx
            yy = y + dy
            if any([xx < 0, xx >= n, yy < 0, yy >= n]):
                continue
            # 방문 했거나 벽이면 계산할 필요 x
            if distance[xx][yy] or arr[xx][yy]:
                continue
            distance[xx][yy] = d + 1
            q.append((xx, yy, d+1))
    return False, 0

def check():
    for i in range(m):
        if start[i]:
            return False
    return True

n, m, power = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 택시의 시작 점
sx, sy = map(int, input().split())
sx, sy = sx-1, sy-1
# 승객의 시작 점, 도착 점
start = []
end = []
for i in range(m):
    x, y, xx, yy = map(int, input().split())
    start.append((x-1, y-1))
    end.append((xx-1, yy-1))

answer = -1
for _ in range(m):

    # 현재 택시의 시작점에서 최단거리를 구한다
    dis = find_dis(sx, sy)

    # 가장 가까운 승객을 선택한다
    temp_dis, temp_x, temp_y, num = find_passenger(dis)

    # 승객있는 곳 까지 가기
    if power >= temp_dis - 1:
        sx, sy = temp_x, temp_y
        power -= (temp_dis - 1)
    else:
        break
    if num == -1:
        break
    # 도착지까지 가기
    ex, ey = end[num]
    flag, spent_power = go_destination(sx, sy, ex, ey)
    if flag and power >= spent_power:
        sx, sy = ex, ey
        power -= spent_power
        start[num] = 0
        end[num] = 0
        # 두 배로 연료 채워주기
        power += (spent_power * 2)
    else:
        break

    if check():
        answer = power
        break

print(answer)