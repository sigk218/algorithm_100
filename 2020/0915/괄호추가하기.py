# https://www.acmicpc.net/problem/16637

import sys
sys.stdin = open('input.txt', 'r')

# 왼쪽에서 부터 순서대로
# 괄호 안에 들어있는 식은 먼저 계산 함

n = int(input())
arr = list(input())

def cal(a, ex, b):
    if ex == '+':
        return int(a) + int(b)
    elif ex == '*':
        return int(a) * int(b)
    else:
        return int(a) - int(b)


def dfs(d, result):
    global answer 
    # print(d, result)
    # 종료 조건 -> 끝까지 가면 최대값 갱신
    if d == n:
        answer = max(answer, result)

    # 초기 조건
    if d == 0:
        dfs(d+1, cal(result, '+', arr[d]))
        if d + 3 <= n:
            dfs(d+3, cal(result, '+', cal(arr[d], arr[d+1], arr[d+2])))
    else:
        if d + 4 <= n:
            dfs(d+4, cal(result, arr[d], cal(arr[d+1], arr[d+2], arr[d+3])))
        if d + 2 <= n:
            dfs(d+2, cal(result, arr[d], arr[d+1]))

answer = (-2) ** 31 + 1
dfs(0, 0)
print(answer)

# 길이 0 일때를 고려하지 않아서 런타임에러남