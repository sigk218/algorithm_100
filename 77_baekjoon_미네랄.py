import sys
sys.stdin = open('input.txt', 'r')

r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]
# print(*arr, sep='\n')
n = int(input())
commands = list(map(int, input().split()))

def down(t, l):
    # 클러스트를 찾는다
    clu = [[] for _ in range(l)]
    visited = [[0 for _ in range(c)] for __ in range(r)]
    # x 값을 기준으로 정렬해서 땅에 안 닿아있는 것들은 내린다
    for i in range(l):
        # print(t[i])
        (x, y) = t[i]
        clu[i].append((x, y))
        visited[x][y] = 1
        q = [(x, y)]
        while q:
            nx, ny = q.pop()
            for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
                xx = nx + dx
                yy = ny + dy
                if 0 <= xx < r and 0 <= yy < c and arr[xx][yy] == 'x' and not visited[xx][yy]:
                    visited[xx][yy] = 1
                    clu[i].append((xx, yy))
                    q.append((xx, yy))
        # 움직여야할 최소값
        bottom = [-1 for _ in range(c)]
        for nx, ny in clu[i]:
            bottom[ny] = max(bottom[ny], nx)
            arr[nx][ny] = '.'
        move_blank = r
        for cc in range(c):
            if bottom[cc] == -1:continue
            rr = bottom[cc]
            while True:
                rr += 1
                if not(0 <= rr < r) or arr[bottom[cc]][rr] == 'x':
                    rr -= 1
                    break
            move_blank = min(move_blank, rr-bottom[cc])
        # print(move_blank)
        for nx, ny in clu[i]:
            arr[nx+move_blank][ny] = 'x'



for i in range(n):
    commands[i] = r - commands[i]
    if i % 2 == 0 or i == 0:
         flag = False
         for j in range(c):
             if arr[commands[i]][j] == 'x':
                 arr[commands[i]][j] = '.'
                 flag = True
                 break
    else:
        for j in range(c-1, -1, -1):
            if arr[commands[i]][j] == 'x':
                arr[commands[i]][j] = '.'
                flag = True
                break
    if flag == False: continue
    num = 0
    t = []
    for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
        tx, ty = commands[i] + dx, j + dy
        if 0 <= tx < r and 0 <= ty < c and arr[tx][ty] == 'x':
            t.append((tx, ty))
            num += 1
    if num > 1:
        down(t, num)
for small in arr:
    for s in small:
        print(s, end='')
    print()