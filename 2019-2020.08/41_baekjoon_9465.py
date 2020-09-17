import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
for tc in range(T):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    maxvalue = [[0 for _ in range(n)]  for _ in range(2)]

    for i in range(n):
        if i == 0:
            maxvalue[0][i] = sticker[0][i]
            maxvalue[1][i] = sticker[1][i]
            continue
        maxvalue[0][i] = max(maxvalue[0][i-1], sticker[0][i]+maxvalue[1][i-1])
        maxvalue[1][i] = max(maxvalue[1][i-1], sticker[1][i]+maxvalue[0][i-1])
    print(max(maxvalue[1][n-1], maxvalue[0][n-1]))