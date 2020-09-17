import sys
sys.stdin = open('input.txt', 'r')

#  가장 처음에 주사위는 모든 면에 0
#  주사위를 굴린다
#  이동한 칸에 쓰여잇는 수가 0 -> 주사위의 바닥면에 쓰여있는 수 복사
#  아니라면 -> 칸에 쓰여있는 수가 주사위의 바닥면으로 복사 -> 칸에 쓰여있는 수는 0
#### 이동 때 마다 상단에 쓰여있는 값을 구하는 프로그램


n, m, x, y, k = map(int, input().split())
mymap = [list(map(int, input().split())) for _ in range(n)]
command = list(map(int, input().split()))


# 동 서 북 남
# 위 상 오 왼 앞 하
rotate = [
    [4, 2, 1, 6, 5, 3],
    [3, 2, 6, 1, 5, 4],
    [5, 1, 3, 4, 6, 2],
    [2, 6, 3, 4, 1, 5]
]
direction = [(0, 1), (0, -1),(-1, 0), (1, 0)]
# 주사위 방향별로 회전 -> 굴린다 -> 새로운 주사위로 설정한다
dice = [0 for _ in range(6)]

for kk in range(k):
    dx, dy = direction[command[kk] - 1]
    x += dx
    y += dy
    # 바깥으로 이동시킬 수 없다
    if not(0 <= x < n and 0 <= y < m):
        x -= dx
        y -= dy
        continue
    # 주사위를 회전 시킨다
    new_dice = [0 for _ in range(6)]
    for i in range(6):
        # print(rotate[command[kk]-1][i]-1)
        new_dice[i] = dice[rotate[command[kk]-1][i]-1]
    if mymap[x][y] == 0:
        mymap[x][y] = new_dice[5]
    else:
        new_dice[5] = mymap[x][y]
        mymap[x][y] = 0
    print(new_dice[0])
    dice = new_dice

