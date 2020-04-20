import sys
sys.stdin = open('input.txt', 'r')

def rotate(d):
    temp = []
    for dd in range(len(d)-1, -1, -1):
        temp.append((d[dd] + 1) % 4)
    return d + temp

n = int(input())
direction = [(0, 1), (-1, 0), (0, -1), (1, 0)]
arr = [[0 for _ in range(101)] for _ in range(101)]
for nn in range(n):
    y, x, d, g = map(int, input().split())
    # print(x, y, d, g)
    arr[x][y] = 1
    first = [d]
    for gg in range(g):
        routes = rotate(first)
        first = routes
    # print(first)
    for dd in first:
        x += direction[dd][0]
        y += direction[dd][1]
        arr[x][y] = 1

answer = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] and arr[i+1][j] and arr[i][j+1] and arr[i+1][j+1]:
            answer += 1
print(answer)


