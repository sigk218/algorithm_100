import sys
sys.stdin = open('input.txt', 'r')


def change(d):
    # 오른 쪽 일 때
    if d == 0:
        return 2
    elif d == 1:
        return 3
    elif d == 2:
        return 0
    else:
        return 1



# 시계 방향으로 90 -> idx - 1
# 0: 우 1: 상 2: 좌 3: 하
direction = [(0, 1), (-1, 0), (0, -1), (1, 0)]
n = int(input())
answer = 0
# 100 * 100 격자
arr = [[0 for _ in range(101)] for _ in range(101)]
for _ in range(n):

    y, x, d, g = map(int, input().split())
    # 1세대 드래곤 커브
    dragon = [(y, x), (y+direction[d][1], x+direction[d][0])]
    dragon_dir = [(d+3)%4]

    for _ in range(g):
        # print(_, '세대입니다')
        new_d = []
        dn = len(dragon_dir)
        for i in range(dn-1, -1, -1):
            idx = dragon_dir[i]
            idx = change(idx)
            # print(idx)
            ny, nx = dragon[-1]
            ny += direction[idx][1]
            nx += direction[idx][0]
            dragon.append((ny, nx))

            new_d.append((idx+3)%4)
        dragon_dir += new_d


    for y, x in dragon:
        if x < 0 or x > 100 or y < 0 or y > 100: continue
        arr[y][x] = 1
    # print(dragon)


visited = [[0 for _ in range(101)] for _ in range(101)]
for j in range(100):
    for i in range(100):
        if visited[i][j]:continue
        if arr[i][j] and arr[i+1][j] and arr[i][j+1] and arr[i+1][j+1]:
            visited[i][j] = 1
            answer += 1
print(answer)

