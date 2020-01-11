import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(T):
    print('#{} '.format(tc+1), end='')
    d, w, k = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(d)]

    def check(film):
        for j in range(w):
            cnt = 0
            t = film[0][j]
            for i in range(1, d):
                if t == film[i][j]:
                    cnt += 1
                elif t != film[i][j]:
                    cnt = 0
                    t = film[i][j]
                if cnt == k-1:
                    break
            else:
                return False
        return True

    def dfs(x, cnt):
        global answer
        if answer <= cnt: return
        if x == d:
            t = []
            for i in range(d):
                if p[i] == -1:
                    t.append(li[i])
                elif p[i] == 0:
                    t.append(drug[0])
                elif p[i] == 1:
                    t.append(drug[1])
            if check(t):
                answer = min(answer, cnt)
            return
        p[x] = -1
        dfs(x+1, cnt)
        p[x] = 0
        dfs(x+1, cnt+1)
        p[x] = 1
        dfs(x+1, cnt+1)

    p = [0] * d
    drug = [[0] * w, [1] * w]
    answer = 10000000
    dfs(0, 0)
    print(answer)