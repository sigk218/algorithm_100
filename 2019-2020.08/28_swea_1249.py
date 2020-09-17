import sys, collections
sys.stdin = open('input.txt', 'r')

def solve(ix, iy):
    visited = [[1000000] * n for _ in range(n)]

    q = collections.deque()
    q.append((ix, iy))
    visited[ix][iy] = 0

    while q:
        x, y = q.popleft()
        for dx, dy in (-1, 0), (1, 0), (0, 1), (0, -1):
            xx = x + dx
            yy = y + dy
            if 0 <= xx < n and 0 <= yy < n and visited[xx][yy] > visited[x][y]+roads[xx][yy]:
                visited[xx][yy] = visited[x][y]+roads[xx][yy]
                q.append((xx, yy))
    return visited[n-1][n-1]

T = int(input())
for tc in range(T):
    n = int(input())
    roads = [list(map(int, input())) for _ in range(n)]
    print('#{} {}'.format(tc+1, solve(0, 0)))
