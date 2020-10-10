import sys
sys.stdin = open('input.txt', 'r')

# https://www.acmicpc.net/problem/1110

n = int(input())

temp = n
idx = 0
while True:
    idx += 1
    # 원래 자리수의 마지막 숫자
    last = temp % 10
    temp //= 10
    first = temp % 10

    next_num = (last + first) % 10
    temp = last * 10 + next_num
    if temp == n:
        break

print(idx)