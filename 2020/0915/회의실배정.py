# https://www.acmicpc.net/problem/1931

import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
arr = []


for _ in range(n):
    start, end = map(int, input().split())
    arr.append((start, end))
    
# 종료 시간을 기준으로 정렬
arr.sort(key=lambda x:(x[1], x[0]))


# 현재 진행중인 회의의 끝나는 시간
temp = arr[0][1]
cnt = 1

for i in range(1, n):
    # 다음 회의의 시작시간이
    # 진행중인 회의의 끝나는 시간보다 크거나 같다면
    if arr[i][0] >= temp:
        cnt += 1
        temp = arr[i][1]
print(cnt)

