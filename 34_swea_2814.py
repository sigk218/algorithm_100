import sys
sys.stdin = open('input.txt', 'r')

def sovle(d, dist):
    global answer

    answer = max(answer, dist)

    for i in range(n):
        if adj[d][i] and not visited[i]:
            visited[i] = 1
            sovle(i, dist+1)
            visited[i] = 0

T = int(input())
for tc in range(T):
    n, m = map(int, input().split())

    adj = [[0] * n for _ in range(n)]
    for mm in range(m):
        i, j = map(int, input().split())
        adj[i-1][j-1] = 1
        adj[j-1][i-1] = 1

    answer = 0
    visited = [0] * n
    for nn in range(n):
        visited[nn] = 1
        sovle(nn, 1)
        visited[nn] = 0
    print('#{} {}'.format(tc+1, answer))


