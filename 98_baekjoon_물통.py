import sys, collections
sys.stdin = open('input.txt', 'r')

A, B, C = map(int, input().split())
visited = [[[0 for _ in range(201)] for __ in range(201)] for ___ in range(201)]

visited[A][B][C] = 1
result = [0 for _ in range(201)]
q = collections.deque()
q.append((0, 0, C))

while q:
    a, b, c = q.popleft()
    if visited[a][b][c]: continue
    visited[a][b][c] = 1
    if a == 0:
        result[c] = 1
    # a -> b
    if a + b > B:
        q.append((a+b-B, B, c))
    else:
        q.append((0, a+b, c))
    # b -> c
    if b + c > C:
        q.append((a, b+c-C, C))
    else:
        q.append((a, 0, b+c))
    # c -> a
    if c + a > A:
        q.append((A, b, c+a-A))
    else:
        q.append((c+a, b, 0))
    # a -> c
    if a+c > C:
        q.append((a+c-C, b, C))
    else:
        q.append((0, b, a+c))
    # b -> a
    if b+a > A:
        q.append((A, b+a-A, c))
    else:
        q.append((b+a, 0, c))
    # c -> b
    if c + b > B:
        q.append((a, B, c+b-B))
    else:
        q.append((a, c+b, 0))

for i in range(201):
    if result[i] == 0:continue
    print(i, end=' ')