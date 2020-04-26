import sys
sys.stdin = open('input.txt', 'r')

n, m, h = map(int, input().split())
arr = [[0 for _ in range(n)] for _ in range(h)]

for _ in range(m):
    i, j = map(int, input().split())
    arr[i-1][j-1] = 1
# print(*arr, sep='\n')
def check():
    for j in range(n):
        start = j
        for i in range(h):
            # print(start, i, arr[i][start])
            if start < n and arr[i][start] == 1:
                start += 1
            elif start-1 >= 0 and arr[i][start-1] == 1:
                start -= 1
        if start != j:
            return False
    return True

# print(check())
def choice(d, x, y):
    global answer
    if d > 3: return
    # print(d, x, y)
    if check():
        answer = min(answer, d)
    for i in range(x, h):
        ny = y if i == x else 0
        for j in range(ny, n):
            if arr[i][j] == 0:
                if j+2 > n: continue
                arr[i][j] = 1
                choice(d+1, i, j+2)
                arr[i][j] = 0
answer = 10
choice(0, 0, 0)
print(-1 if answer == 10 else answer)