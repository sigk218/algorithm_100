import sys, collections
sys.stdin = open('input.txt', 'r')

# 몇일이 지나면 토마토가 다 익게 되는지(최소 일수)
def check(li):
    for hh in range(h):
        for nn in range(n):
            for mm in range(m):
                if li[hh][nn][mm] == 0:
                    return False
    return True

def fulltoma(tomatos):
    fulltoma = []
    for hh in range(h):
        for nn in range(n):
            for mm in range(m):
                if tomatos[hh][nn][mm] == 1:
                    fulltoma.append((hh, nn, mm))
    return fulltoma
def solve(fulltoma):
    q = collections.deque()
    for sz, sx, sy in fulltoma:
        q.append((sz, sx, sy, 0))
    # print(q)
    while q:
        z, x, y, d = q.popleft()
        # print(z, x, y, d)
        # print(*tomatos, sep='\n')
        # 위, 아래, 왼쪽, 오른쪽, 앞, 뒤
        for dz, dx, dy in (0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0):
            xx = x + dx
            yy = y + dy
            zz = z + dz
            if 0 <= xx < n and 0 <= yy < m and 0 <= zz < h:
                if tomatos[zz][xx][yy] == 0:
                    tomatos[zz][xx][yy] = 1
                    q.append((zz, xx, yy, d+1))
    if check(tomatos):
        return d
    return -1

# 토마토가 모두 익어있으면 0, 모두 익지 못하는 상황이면 -1을 출력해야함

m, n, h = map(int, input().split())

tomatos = [list(list(map(int, input().split())) for _ in range(n)) for __ in range(h)]


# 처음에 토마토가 모두 익었으면 0
temp = solve(fulltoma(tomatos))
print(temp)


