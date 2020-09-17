import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

a, b, c = map(int, input().split())

total = a + b + c
# 합이 3으로 나눠지지 않으면 불가
if total % 3 != 0:
    print(0)
    exit()
# a, b만 체크해줄 배열
check = [[0 for _ in range(total+1)] for _ in range(total+1)]
check[a][b] = 1
q = deque()
q.append((a, b, c))
while q:
    aa, bb, cc = q.popleft()
    if aa == bb == cc:
        print(1)
        exit()
    for nx, ny in [(aa, bb), (bb, cc), (aa, cc)]:
        # nx가 큰수
        if nx < ny:
            nx, ny = ny, nx
        na = nx - ny
        nb = ny + ny
        nc = total-na-nb
        if not check[na][nb]:
            check[na][nb] = 1
            q.append((na, nb, nc))
print(0)