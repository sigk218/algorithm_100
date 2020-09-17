T = int(input())
for tc in range(T):
    print('#{} '.format(tc + 1), end='')
    n = int(input())
    li = [list(map(int, input().split())) for _ in range(n)]

    people = []
    stairs = []
    for i in range(n):
        for j in range(n):
            if li[i][j] == 1:
                people.append((i, j))
            elif 2 <= li[i][j] <= 10:
                stairs.append((i, j))

    pn = len(people)
    dif1 = []
    dif2 = []
    for px, py in people:
        dif1.append(abs(stairs[0][0] - px) + abs(stairs[0][1] - py))
        dif2.append(abs(stairs[1][0] - px) + abs(stairs[1][1] - py))


    def finddis(t, s):
        tt = t[:]
        n = len(t)
        ins = [0] * n # 계단 + 사람
        cnt = 0
        while sum(tt) < 1000 * n:
            cnt += 1
            for i in range(n):
                #print(tt, ins)
                if tt[i] == -s:
                    tt[i] = 1000
                    ins[i] = 0
                if tt[i] != 1000:
                    tt[i] -= 1
                if tt[i] < 0:
                    ins[i] = 1
                if sum(ins) > 3:
                    tt[i] = 0
                    ins[i] = 0
        return cnt


    def subset(d):
        global answer
        if d == pn:
            d1 = finddis(sorted(t1), li[stairs[0][0]][stairs[0][1]])
            d2 = finddis(sorted(t2), li[stairs[1][0]][stairs[1][1]])
            answer = min(max(d1, d2), answer)
        else:
            if not visited[d]:
                visited[d] = 1
                t1.append(dif1[d])
                subset(d + 1)
                t1.pop()
                t2.append(dif2[d])
                visited[d] = 0
                subset(d + 1)
                t2.pop()


    answer = 10000
    visited = [0] * pn
    t1 = []
    t2 = []
    subset(0)
    print(answer)