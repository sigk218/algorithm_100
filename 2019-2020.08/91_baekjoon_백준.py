n, m = map(int, input().split())
# 좌표를 들고 이동해야 한다 ? -> 보드는 계속 그대로 있으니까
arr = [list(input()) for _ in range(n)]
# print(*arr, sep='\n')
def out(x, y):
    if 0 <= x < n and 0 <= y < m: return False
    else: return True

x1, y1, x2, y2 = -1, -1, -1, -1
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'o':
            if x1 == -1:
                x1, y1 = i, j
                arr[i][j] = '.'
            else:
                x2, y2 = i, j
                arr[i][j] = '.'
                break
def go(d, x1, y1, x2, y2):
    global answer
    if d == 11:
        return
    if out(x1, y1) and out(x2, y2):
        return
    if out(x1, y1) or out(x2, y2):
        if answer != -1:
            answer = min(answer, d)
        else:
            answer = d
    else:
        for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
            xx1, yy1 = x1 + dx, y1 + dy
            xx2, yy2 = x2 + dx, y2 + dy
            if not out(xx1, yy1) and arr[xx1][yy1] == '#':
                xx1, yy1 = x1, y1
            if not out(xx2, yy2) and arr[xx2][yy2] == '#':
                xx2, yy2 = x2, y2
            if out(xx1, yy1) and out(xx2, yy2):
                continue
            go(d+1, xx1, yy1, xx2, yy2)

answer = -1
go(0, x1, y1, x2, y2)
print(answer)