import sys
sys.stdin = open('input.txt', 'r')

T = 10
for tc in range(T):
    n = int(input())
    houses = list(map(int, input().split()))

    cnt = 0
    for nn in range(2, n-2):
        high = max(max(houses[nn-2:nn]), max(houses[nn+1:nn+3]))
        if houses[nn] > high:
            cnt += houses[nn]- high
    print('#{} {}'.format(tc+1, cnt))