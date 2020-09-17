import sys
sys.stdin = open('input.txt', 'r')
'''
T = int(input())
for tc in range(T):
    n = int(input())

    def solve(d):
        global cnt
        if d > n: return
        if d == n:
            cnt += 1
        else:
            solve(d+1)
            solve(d+2)
            solve(d+3)

    cnt = 0
    solve(0)
    print(cnt)
    # 재귀 풀이 시 완료조건 줄 것

'''
T = int(input())
for tc in range(T):
    n = int(input())
    cnt = [0 for _ in range(n+1)]

    for i in range(1, n+1):
        if i == 1:
            cnt[i] = 1
            continue
        elif i == 2:
            cnt[i] = 2
            continue
        elif i == 3:
            cnt[i] = 4
            continue
        cnt[i] = cnt[i-1] + cnt[i-2] + cnt[i-3]
        # print(cnt)
    print(cnt[n])