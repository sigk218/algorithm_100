import sys
sys.stdin = open('input.txt', 'r')

# r, c 는 1 부터
# 치킨거리 : 집과 가장 가까운 치킨집 사이의 거리
# 도시의 치킨거리 : 모든 집의 치킨 거리의 합
# 치킨 M개를 고른다
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
house = []
chicken = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            house.append((i, j))
        elif arr[i][j] == 2:
            chicken.append((i, j))
def dis(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)
cnum = len(chicken)
hnum = len(house)

def solve(d):
    global ans, t
    if d > m: return
    if d == m:
        # print('도착!')
        k = -1
        temp = [10000000 for _ in range(len(house))]
        for hx, hy in house:
            k += 1
            for cx, cy in t:
                temp[k] = min(temp[k], dis(hx, hy, cx, cy))
        # print(temp)
        ans = min(ans, sum(temp))
    else:
        for i in range(cnum):
            if visited[i] == 0:
                visited[i] = 1
                t.append(chicken[i])
                solve(d+1)
                t.pop()
                visited[i] = 0

t=[]
ans = 100000000
visited = [0 for i in range(cnum)]
solve(0)
print(ans)
