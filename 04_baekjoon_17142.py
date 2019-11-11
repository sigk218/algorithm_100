n, m = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]

blank_cnt = 0
virus_num = 0
virus = []
for i in range(n):
    for j in range(n):
        if li[i][j] == 2:
            virus_num += 1
            virus.append([i, j, 0])
        elif li[i][j] == 0:
            blank_cnt += 1

def spread(virus):
    global mintime
    v_li = []
    v_bi = dict()
    num = 0
    for x, y, active in virus:
        if active == 1:
            v_li.append((x, y, 0))
            v_bi[(x, y)] =1
        else:
            v_bi[(x, y)] = 0

    while v_li:
        x, y, d = v_li.pop(0)
        if num == blank_cnt:
            if len(v_li) > 0:
                i, j, time = v_li.pop()
            else:
                time = d
            mintime = min(mintime, time)
            return

        for dx, dy in (0, 1), (0, -1), (-1, 0), (1, 0):
            xx = x+dx
            yy = y+dy
            if 0 <= xx < n and 0 <= yy < n and li[xx][yy] != 1 and v_bi.get((xx, yy)) != 1:
                if v_bi.get((xx, yy)) == 0:
                    pass
                else:
                    num += 1
                v_li.append((xx, yy, d+1))
                v_bi[(xx, yy)] = 1

def pick(x, s):
    global answer, cnt

    if x == m:
        spread(virus)
        return
    else:
        for i in range(s, virus_num):
            if not virus[i][2]:
                virus[i][2] = 1
                pick(x+1, i)
                virus[i][2] = 0
cnt = 0
mintime = 10000000
pick(0, 0)
print(mintime if mintime < 10000000 else -1)