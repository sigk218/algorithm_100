import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def solve(end_day, money):
    global answer

    answer = max(answer, money)

    for i in range(end_day, n):
        if i + arr[i][0] > n: continue
        solve(i+arr[i][0], money+arr[i][1])

answer = -1
solve(0, 0)
print(answer)