import sys
sys.stdin = open('input.txt', 'r')

n, m, h = map(int, input().split())

ladder = [[0 for _ in range(n+1)] for __ in range(h+1)]
for mm in range(m):
    i, j = map(int, input().split())
    ladder[i][j] = 1

# 사다리 내려감
def down(start):
    for hh in range(h+1):
        # print(mm, start)
        dif = 0
        if start == 1:
            if ladder[hh][start]:
                dif += 1
        elif start == n:
            if ladder[hh][start-1]:
                dif -= 1
        else:
            if ladder[hh][start-1]:
                dif -= 1
            if ladder[hh][start]:
                dif += 1
        start += dif
    # 끝을 반환함
    return start


# 가로로 사다리를 놓음
def pick(row, d):
    global ans
    if d > 3: return
    for j in range(row, n):
        end = down(j)
        if j != end:
            break
    else:
        ans = min(ans, d)
    for (i, j), v in visited.items():
        if ladder[i][j] == 0:
            ladder[i][j] = 1
            pick(d+1)
            ladder[i][j] = 0


visited = dict()
for i in range(1, h+1):
    for j in range(1, n):
        if ladder[i][j] == 0:
            visited[(i, j)] = 0
ans = 1000000000
res = pick(1, 0)
print(ans if ans != 1000000000 else -1)

