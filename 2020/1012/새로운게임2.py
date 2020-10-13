import sys
sys.stdin = open('input.txt', 'r')

def check():
    # 말이 4개이상 쌓이면 종료
    for i in range(n):
        for j in range(n):
            if len(visited[i][j]) > 3:
                return True
    return False

def blue(x, y, d, temp_horse):
    # 이동 방향을 반대로 하고, 한 칸 이동
    # 방향을 바꾼후에 이동하려는 칸이 파란색인 경우 ? 이동하지 않고 가만히 있는다
    if d == 0:
        nd = 1
    elif d == 1:
        nd = 0
    elif d == 2:
        nd = 3
    else:
        nd = 2


    nx, ny = x + dir[nd][0], y + dir[nd][1]

    if nx < 0 or nx >= n or ny < 0 or ny >= n:
        visited[x][y] += temp_horse
        return x, y, nd
    if arr[nx][ny] == 2:
        visited[x][y] += temp_horse
        return x, y, nd
    if arr[nx][ny] == 1:
        red(nx, ny, temp_horse)
        return nx, ny, nd
    elif arr[nx][ny] == 0:
        white(nx, ny, temp_horse)
        return nx, ny, nd



def red(x, y, temp_horse):

    temp_horse.reverse()
    visited[x][y] += temp_horse
    return

def white(x, y, temp_horse):

    visited[x][y] += temp_horse
    return


n, k = map(int, input().split())

# 0 : 흰색, 1 : 빨간색, 2 : 파란색
arr = [list(map(int, input().split())) for _ in range(n)]

dir = [(0, 1), (0, -1), (-1, 0), (1, 0)]
horse = [[] for _ in range(k)]
# 몇 번말이 있는지
visited = [[[] for _ in range(n)] for _ in range(n)]

for i in range(k):
    x, y, d = map(int, input().split())
    horse[i] = [x-1, y-1, d-1]
    visited[x-1][y-1] = [i+1]


for turn in range(1000):
    # 말이 4개이상 쌓이는 순간 종료
    # print(*visited, sep='\n')

    # 모든 말이 순서대로 이동한다.
    for i in range(k):
        # visited -> 업힌 말의 관계 표시
        # horse -> 순서대로 말 표시

        # 이동하려는 말
        (x, y, d) = horse[i]
        temp_idx = visited[x][y].index(i + 1)
        # 내 뒤에 업힌 말들 !
        temp_horse = visited[x][y][temp_idx:]
        visited[x][y] = visited[x][y][:temp_idx]

        nd = d

        nx, ny = x + dir[d][0], y + dir[d][1]
        # 체스판을 벗어나거나 파란색인 경우
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            nx, ny, nd = blue(x, y, d, temp_horse)
        elif arr[nx][ny] == 2:
            nx, ny, nd = blue(x, y, d, temp_horse)

        # 빨간색인 경우
        elif arr[nx][ny] == 1:
            red(nx, ny, temp_horse)

        # 흰색인 경우
        elif arr[nx][ny] == 0:
            white(nx, ny, temp_horse)

        # 그 위에 말들의 좌표를 다 바꿔줘야함 !
        for num in temp_horse:
            horse[num - 1][0] = nx
            horse[num - 1][1] = ny

        horse[i] = [nx, ny, nd]
        if check():
            print(turn+1)
            exit()

print(-1)

# 턴이 진행되던 중에 말이 4개이상 쌓이는 순간 게임이 종료됨 : 문제를 잘 읽자 (시점, 조건)