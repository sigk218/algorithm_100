# https://www.acmicpc.net/problem/1475

import sys
sys.stdin = open('input.txt', 'r')

# 하나씩 돌면서 추가한다
number = list(map(int, list(input())))

check = [0 for _ in range(10)]

for n in number:

    if n == 6 or n == 9:
        # 빈 곳 중 아무데나
        if check[6] < check[9]:
            check[6] += 1
            continue
        elif check[6] > check[9]:
            check[9] += 1
            continue

    check[n] += 1

print(max(check))


