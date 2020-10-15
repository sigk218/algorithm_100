import sys
sys.stdin = open('input.txt', 'r')

def spread(cell_list):
    global cell
    new_cell = dict()

    for x, y in cell_list:
        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            xx = x + dx
            yy = y + dy
            # 아무것도 없는 칸일 때
            if cell.get((xx, yy)):
                continue
            if new_cell.get((xx, yy)) == None:
                new_cell[(xx, yy)] = [cell[(x, y)][0], 0, 0]
            elif new_cell[(xx, yy)][0] < cell[(x, y)][0]:
                new_cell[(xx, yy)] = [cell[(x, y)][0], 0, 0]
    # print(len(new_cell), '개 새로 추가')
    # print(new_cell)
    return new_cell

# 줄기세포 : 생명력
# X 시간동안 비활성 상태, X 시간이 지나는 순간 활성 상태, X 시간동안 살아있다가 죽음
# 활성상태가 되고 한 턴 소비함!
# 초부터 세야하나 ?

t = int(input())
for tc in range(1, t+1):
    cell = dict()
    n, m, k = map(int, input().split())

    for i in range(n):
        t = list(map(int, input().split()))
        for j in range(m):
            if t[j] == 0: continue
            # 생명력, 상태, 초
            cell[(i, j)] = [t[j], 0, 0]

    for _ in range(k):
        # print(_+1, '시간후')
        new_cell = []
        for (x, y), (power, state, second) in cell.items():
            if state == 2:
                continue
            # 시간 먹기
            cell[(x, y)] = [power, state, second+1]
            second += 1
            # 검사 하기
            if all([state == 0,second == power]):
                # 비 활성 상태이고 시간이 다 흘렀다면
                cell[(x, y)] = [power, 1, 0]
            if all([state == 1, second == 1]):
                # 활성 상태이고 시간이 1초 흘렀다면 번식한다
                new_cell.append((x, y))
            if all([state == 1, second == power]):
                # 활성 상태이고 시간이 다 흘렀다면
                cell[(x, y)] = [power, 2, 0]


        # 번식 하기
        cell.update(spread(new_cell))
        # print(cell)
        # print(len(cell))
    cnt = 0
    for k, v in cell.items():
        if v[1] == 2:continue
        cnt += 1
    print('#{} {}'.format(tc, cnt))