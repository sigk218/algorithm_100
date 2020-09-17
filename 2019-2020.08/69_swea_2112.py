import sys
sys.stdin = open('input.txt', 'r')

# 단면의 모든 세로 방향에 대해서 동일한 특성의 셀들이 
# K 개 이상 연속적으로 있는 경우에만 성능 검사 통과

# 체크하는 함수
# 모든 세로 방향에 대해 동일한 특성의 셀들이 K개 이상 연속적으로 있는지
def check(films):
    for ww in range(w):
        dd = 0
        flag = False
        while dd < d:
            start = films[dd][ww]
            if dd + k - 1 >= d: return False
            for kk in range(k-1):
                dd += 1
                if start != films[dd][ww]:
                    break
            else:
                flag = True
                break
        if flag == False:
            return False
    return True
#  가로로 a, b 투입
def solve(dep, cnt):
    global ans
    if ans <= cnt: return
    if dep == d:
        t = []
        for dd in range(d):
            if p[dd] == -1:
                t.append(films[dd])
            elif p[dd] == 0:
                t.append(W)
            elif p[dd] == 1:
                t.append(R)
        if check(t):
            ans = min(ans, cnt)
        return
    else:
        p[dep] = -1
        solve(dep + 1, cnt)
        p[dep] = 0
        solve(dep + 1, cnt+1)
        p[dep] = 1
        solve(dep + 1, cnt+1)

T = int(input())
for t in range(T):
    d, w, k = map(int, input().split())
    films = [list(map(int, input().split())) for _ in range(d)]
    p = [0 for _ in range(d)]
    W = [0 for _ in range(w)]
    R = [1 for _ in range(w)]
    ans = 100000000
    solve(0, 0)
    print('#{} {}'.format(t+1, ans))