# https://www.acmicpc.net/problem/16637

import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
ex = list(input())

def cal(a, ex, b):
    if ex == '+':
        return a+b
    elif ex == '-':
        return a-b
    else:
        return a*b


# d = 현재까지 index, temp : 현재까지 계산 값
def dfs(d, temp):
    global answer
    if d == n:
        answer = max(answer, temp)
        return
    # 첫 번째 항에 대해서
    if d == 0:
        dfs(d+1, cal(temp, '+', int(ex[d])))
        if d+3 <= n:
            dfs(d+3, cal(int(ex[d]), ex[d+1], int(ex[d+2])))
            return
    if d + 2 <= n:
        dfs(d+2, cal(temp, ex[d], int(ex[d+1])))
    if d + 4 <= n:
        dfs(d+4, cal(temp, ex[d], cal(int(ex[d+1]), ex[d+2], int(ex[d+3]))))

answer = - (2 ** 31)
dfs(0, 0)
print(answer)

