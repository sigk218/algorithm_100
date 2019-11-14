import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(T):
    print('#{} '.format(tc+1), end='')
    n, m, k = map(int, input().split())

    sepo = dict()
    for i in range(n):
        t = list(map(int, input().split()))
        for j in range(m):
            if t[j] == 0: continue
            sepo[(i, j)] = [t[j], t[j], 0] # 생명, count, 죽었는지

    def spread(x, y, value):
        for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
            nx = x + dx
            ny = y + dy
            if not temp.get((nx, ny)):
                if not sepo.get((nx, ny)):
                    temp[(nx, ny)] = [value[0], value[0], 0]
            else:
                if temp.get((nx, ny))[0] < value[0]:
                    temp[(nx, ny)] = [value[0], value[0], 0]

    for kk in range(k):
        temp = dict()
        for key, value in sepo.items():
            if value[2] == 1: continue
            value[1] -= 1
            if value[1] == -1: # 활성 상태일때
                spread(key[0], key[1], value)
            if value[0] == -(value[1]):# 죽일 것임.
                value[2] = 1
        sepo.update(temp)

    cnt = 0
    for key, value in sepo.items():
        if value[2] == 0:
            cnt += 1
    print(cnt)