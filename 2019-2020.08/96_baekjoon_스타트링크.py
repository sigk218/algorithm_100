import sys
sys.stdin = open('input.txt', 'r')

f, s, g, u, d = map(int, input().split())

visited = [0 for _ in range(f+1)]

q = [(s, 0)]
visited[s] = 1
flag = False
while q:
    x, cnt = q.pop(0)
    if x == g:
        flag = True
        break
    for dx in u, -d:
        xx = x + dx
        if 1 <= xx <= f and not visited[xx]:
            visited[xx] = 1
            q.append((xx, cnt+1))
if flag:
    print(cnt)
else:
    print('use the stairs')