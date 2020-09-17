import sys, collections
sys.stdin = open('input.txt', 'r')

def solve(start):
    global temp
    visited = [0] * n
    q = collections.deque()
    q.append((start, 0))
    visited[start] = 1

    temp = {i: [] for i in range(n)}
    temp[0].append(start)

    while q:
        person, d = q.popleft()
        if adj[person]:
            for p in adj[person]:
                if not visited[p]:
                    visited[p] = 1
                    q.append((p, d+1))
                    temp[d+1].append(p)
    return d



T = 10
for tc in range(T):
    n = 100 + 1
    length, start = map(int, input().split())

    adj = {i: [] for i in range(n)}

    adj_temp = list(map(int, input().split()))
    for i in range(0, length-1, 2):
        adj[adj_temp[i]].append(adj_temp[i+1])
    last = solve(start)
    print('#{} {}'.format(tc+1, sorted(temp[last], reverse=True)[0]))

