import sys
sys.stdin = open('input.txt', 'r')

T = 10
for tc in range(T):
    n = int(input())
    boxs = list(map(int, input().split()))

    for i in range(n):
        top = max(boxs)
        bottom = min(boxs)
        if top - bottom <= 1:
            break
        boxs[boxs.index(top)] -= 1
        boxs[boxs.index(bottom)] += 1

    print('#{} {}'.format(tc+1, max(boxs)-min(boxs)))
