import sys
sys.stdin = open('input.txt', 'r')

# 동시에 번식 하려고 하는 경우 생명력 수치가 높은 게 그리드를 차지 하게 됨.

T = int(input())
for tc in range(1):
    n, m, k = map(int, input().split())
    mymap = [[0 for _ in range(k * 2 + m + 1)] for _ in range(k * 2 + n + 1)]

    cell = dict()
    # 그리드 상태가 주어짐 k 만큼 더해서 그리드에 표시해준다.
    for i in range(n):
        temp = list(map(int, input().split()))
        for j in range(m):
            if temp[j] == 0 : continue
            mymap[i+k][j+k] = temp[j]
            # 좌표, 생명력, 상태 : -1 (죽음), 0 (비활성), 1(활성), 2(번식)
            cell[(i+k, j+k)] = [temp[j], 0, 0]

    def spread():
        new_cell = dict()
        for (x, y), (life, time, state) in cell.items():
            # 죽은 세포는 넘어간다
            if state == -1: continue

            # 번식 가능한 세포 일 경우
            if state == 2:
                cell[(x, y)] = [life, 0, 1]
                for dx, dy in (0, 1), (-1, 0), (0, -1), (1, 0):
                    xx = x + dx
                    yy = y + dy
                    # 조건을 잘 줘야함!
                    if cell.get((xx, yy)) == None:
                        # 상태 바꿔주기 -> for 문이 도는 동안 life를 건드리면 안된다.
                        if new_cell.get((xx, yy)):
                            # print(xx, yy, life)
                            # life = max(life, new_cell[(xx, yy)][0])
                            new_cell[(xx, yy)][0] = max(life, new_cell[(xx, yy)][0])
                            mymap[xx][yy] = new_cell[(xx, yy)][0]
                        else:
                            # 맵에 표시 해주기
                            new_cell[(xx, yy)] = [life, 0, 0]
                            mymap[xx][yy] = life


            cell[(x, y)][1] += 1

            # time이 꽉 찾을 경우
            if cell[(x, y)][1] == cell[(x, y)][0]:
                # 비 활성일 경우 -> 번식
                if cell[(x, y)][2] == 0:
                    cell[(x, y)] = [cell[(x, y)][0], 0, 2]
                # 활성일 경우 -> 사망
                elif cell[(x, y)][2] == 1:
                    # print(x, y)
                    cell[(x, y)] = [cell[(x, y)][0], 0, -1]
        cell.update(new_cell)

    for kk in range(k):
        spread()

    cnt = 0
    for (x, y), (life, time, state) in cell.items():

        if state == -1: continue
        cnt += 1
    # print(cell)
    print('#{} {}'.format(tc+1, cnt))