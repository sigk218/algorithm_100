import sys
sys.stdin = open('input.txt', 'r')

# 모든 도로의 거리는 1이다 -> bfs로 최단거리 가능 
# x로 부터 출발하여 K인 모든 도시들의 번호
# 존재하지 않으면 -1을 출력한다

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

import collections
distance = [0 for _ in range(n+1)]

q = collections.deque()
q.append((x, 1))
distance[0] = 1
distance[x] = 1

answer = []
while q:
    xx, d = q.popleft()
    if d == k+1:
        answer.append(xx)
    for nx in graph[xx]:
        if distance[nx]:continue
        distance[nx] = d+1
        q.append((nx, d+1))

answer.sort()
if answer:
    for a in answer:
        print(a)
else:
    print(-1)
