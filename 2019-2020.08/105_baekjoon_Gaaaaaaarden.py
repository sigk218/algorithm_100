import sys
sys.stdin = open('input.txt', 'r')

n, m, g, r = map(int, input().split())
#  0: 호수, 1: 배양액을 뿌릴 수 없는 땅, 2: 배양액을 뿌릴 수 있는 땅
arr = [list(map(int, input().split())) for _ in range(n)]

possible = []

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            possible.append((i, j))
# print(*arr, sep='\n')
'''
['g', 'r', 'g', 0, 0, 'r', 'g', 0]
[(0, 3), (0, 5), (1, 6), (2, 0), (3, 2), (3, 4), (4, 1), (4, 6)]
'''


import collections, datetime
st = datetime.datetime.now()
def spread():
    global selected_g, selected_r
    temp = 0
    # print(selected_r, selected_g)
    # g, b, 8
    flower = [[0 for _ in range(m)] for __ in range(n)]
    # 거리 체크
    dist = [[0 for _ in range(m)] for __ in range(n)]
    q = collections.deque()
    # print(visited, possible)
    for s in selected_g:
        (xi, yi) = possible[s]
        q.append((xi, yi, 'g'))
        flower[xi][yi] = 'g'
        dist[xi][yi] = 1

    for s in selected_r:
        (xi, yi) = possible[s]
        q.append((xi, yi, 'r'))
        flower[xi][yi] = 'r'
        dist[xi][yi] = 1

    # for i in range(N):
    #     if visited[i]:
    #         (xi, yi) = possible[i]
    #         q.append((xi, yi, visited[i]))
    #         flower[xi][yi] = visited[i]
    #         dist[xi][yi] = 1

    while q:
        x, y, color = q.popleft()
        # 양쪽에서 넣는데, 꽃이 되어있는 것이 이전에 들어있었을 수 있음
        if flower[x][y] == 8:continue
        for dx, dy in (0, 1), (-1, 0), (0, -1), (1, 0):
            xx = x + dx
            yy = y + dy
            if not(0 <= xx < n and 0 <= yy < m): continue
            if flower[xx][yy] == 8:continue
            if flower[xx][yy] == color: continue
            if arr[xx][yy] == 0: continue

            if not flower[xx][yy]:
                flower[xx][yy] = color
                dist[xx][yy] = dist[x][y] + 1
                q.append((xx, yy, color))
            elif flower[xx][yy] != color:
                if dist[xx][yy] == dist[x][y] + 1:
                    flower[xx][yy] = 8
                    temp += 1

    return temp

# 0: 호수, 1:뿌릴수 X, 2: 뿌릴수 o
# arr = [[0, 0, 0, 0, 1],
#        [0, 0, 0, 0, 2],
#        [1, 2, 2, 1, 1],
#        [2, 1, 2, 0, 1],
#        [0, 1, 0, 0, 1]]

# visited = ['g', 'r', 'g', 0, 0, 'r', 'g', 0]
# spread()

# def pickred(d, start):
#     global visited
#     if d == r:
#         # print('빨간색 다 뽑음')
#         pickgreen(0, 0)
#     else:
#         for i in range(N):
#             if not visited[i]:
#                 visited[i] = 'r'
#                 pickred(d+1, i)
#                 visited[i] = 0
#
# def pickgreen(d, start):
#     global visited, answer
#     if d == g:
#         # print('두개 다 뽑음', visited)
#         answer = max(spread(), answer)
#     else:
#         for i in range(start, N):
#             if not visited[i]:
#                 visited[i] = 'g'
#                 pickgreen(d+1, i)
#                 visited[i] = 0
answer = 0
import itertools
for c1 in itertools.combinations(range(len(possible)), r+g):
    for c2 in itertools.combinations(range(r+g), r):
        selected_r = []
        selected_g = []
        for i in range(r+g):
            if i in c2: selected_r.append(c1[i])
            else: selected_g.append(c1[i])
        answer = max(answer, spread())

N = len(possible)
visited = [0 for i in range(N)]


print(answer)
print(datetime.datetime.now() - st)