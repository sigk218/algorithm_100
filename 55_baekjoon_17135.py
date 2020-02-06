import sys, copy
sys.stdin = open('input.txt', 'r')


# 2. 궁수의 위치 정하기 (3명) 궁수를 어디서 뽑는지 잘 볼 것 !!(m)

def select(start, original):
    global answer

    if sum(visited) == 3:
        temp = []
        for i in range(m):
            if visited[i]: temp.append(i)

    # 5. 보드에 적이 남아있지 않을 때 까지 3~4를 반복
        cnt = 0
        enermies = copy.deepcopy(original)
        while len(enermies) > 0:
            next_enermies, tcnt = attack(temp, enermies)
            enermies = move(next_enermies)
            cnt += tcnt
            # print(enermies)
        # 7. 최대값 구하기
        answer = max(answer, cnt)
    else:
        for i in range(start, m):
            if not visited[i]:
                visited[i] = 1
                select(i, original)
                visited[i] = 0
# select(0)


# 3. 공격
# - 모든 궁수를 동시에
# - 거리가 d 이하인 적중에 가장 가까운 적
# - d가 같다면 가장 왼쪽에 잇는 적
def attack(gslist, enermies):
# 궁수별로 죽일 수 있는 적
    ispossible = {(n, i):[] for i in gslist}
    out = []
    for gy in gslist:
        q = []
        q.append((0, gy, n))
        temp = []
        tempdepth = -1
        while q:
            d, y, x = q.pop(0)
            if d == depth or d == tempdepth:
                break
            for dx, dy in (0, -1), (0, 1), (-1, 0), (1, 0):
                xx = x + dx
                yy = y + dy
                if 0 <= xx < n and 0 <= yy < m:
                    q.append((d+1, yy, xx))
                    if enermies.get((xx, yy)) == 1:
                        tempdepth = d+1
                        temp.append((d+1, yy, xx))
        temp.sort()
        # print(answer)
        # x, y 값을 바꿔준다
        if len(temp) > 0:
            out.append((temp[0][2], temp[0][1]))
    out = set(out)
# 6. 공격해서 죽인 적만 개수 구하기
    for (x, y) in out:
        del enermies[(x, y)]
    # print(out)
    return enermies, len(out)

# 4. 이동
def move(enermies):
    new_enermies = dict()
    for (x, y), die in enermies.items():
        if x + 1 >= n:
            continue
        else:
            new_enermies[(x + 1, y)] = 1
    return new_enermies

n, m, depth = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]

# 1. 적의 위치 받아오기
enermies = dict()
for i in range(n):
    for j in range(m):
        if li[i][j] == 1:
            # 살아있을 때는 1로 하기
            enermies[(i, j)] = 1


visited = [0] * m
answer = 0
select(0, enermies)
print(answer)