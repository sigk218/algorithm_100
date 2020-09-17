import sys, collections
sys.stdin = open('input.txt', 'r')

def bfs():
    global flag
    visited = {i: 0 for i in range(100)}
    q = collections.deque()
    q.append(0)
    visited[0] = 1

    while q:
        node = q.popleft()
        if node == 99:
            flag = 1
            return
        if adj[node]:
            for n in adj[node]:
                if not visited[n]:
                    visited[n] = 1
                    q.append(n)


T = 10
for _ in range(T):
    # 길의 총 개수
    tc, n = map(int, input().split())
    adj = {i: [] for i in range(100)}
    temp = list(map(int, input().split()))

    for i in range(0, len(temp), 2):
        adj[temp[i]].append(temp[i+1])
    flag = 0
    bfs()
    print('#{} {}'.format(tc, flag))