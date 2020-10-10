import sys
sys.stdin = open('input.txt', 'r')

import collections
T = int(input())
for tc in range(1, T+1):

    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    # 집의 갯수
    answer = 0
    for i in range(n):
        for j in range(n):
            visited = [[0 for _ in range(n)] for _ in range(n)]
            q = collections.deque()
            k = 1
            q.append((i, j, k))
            visited[i][j] = k


            house = arr[i][j]
            while q:
                x, y, d = q.popleft()
                if d == k:
                    if (house * m) - (k * k + (k - 1) * (k - 1)) >= 0:
                        answer = max(answer, house)
                    k += 1
                for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
                    xx = x + dx
                    yy = y + dy
                    if xx < 0 or xx >= n or yy < 0 or yy >= n: continue
                    if visited[xx][yy]: continue
                    if arr[xx][yy]:
                        house += 1
                    visited[xx][yy] = d + 1
                    q.append((xx, yy, d + 1))


    print('#'+str(tc)+' '+str(answer))



# 문제 꼼꼼히 읽고, 설정 잘 해줄 것..!
# bfs 초기값 설정 !
# 0도 포함함 !