import sys
sys.stdin = open('input.txt', 'r')

# 거스름돈 개수가 가장 적게 잔돈을 준다

rest = 1000 - int(input())

spare = [500, 100, 50, 10, 5, 1]
cnt = 0

while rest:
    for coin in spare:
        if rest >= coin:
            temp = rest // coin
            cnt += temp
            rest -= temp * coin

print(cnt)

