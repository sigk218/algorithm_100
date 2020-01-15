import sys
sys.stdin = open('input.txt', 'r')


def default():
    global cnt
    for mm in range(m):
        if flag[0][mm] != 'W':
            cnt += 1
        if flag[n-1][mm] != 'R':
            cnt += 1
    return cnt

def solve(d, color, cnt):
    global temp
    # print(temp)
    # print(d, color, cnt)
    if d == n - 2:
        print('end', cnt)
        print(temp)
    else:
        for mm in range(m):
            if flag[d][mm] != color:
                cnt += 1
        temp.append('B')
        solve(d + 1, 'B', cnt)
        temp.pop()
        if color == 'W':
            if d < n - 2:
                temp.append('w')
                solve(d+1, 'W', cnt)
                temp.pop()
        elif color == 'B':
            temp.append('R')
            solve(d+1, 'R', cnt)
            temp.pop()


T = int(input())

n, m = map(int, input().split())
flag = [list(input()) for _ in range(n)]
check = ['W'] + ['' for _ in range(n-2)] + ['R']
temp = []
solve(0, 'W', 0)
cnt = 0
print(default())
