import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(T):

    n = int(input())
    land = [list(map(int, input())) for _ in range(n)]

    full = n // 2
    money = 0
    for i in range(n):
        if i <= full:
            start = full-i
        else:
            start = i-full
        for j in range(start, n-start):
            money += land[i][j]
    print('#{} {}'.format(tc+1, money))

