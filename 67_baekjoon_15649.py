n, m = map(int, input().split())

def solve(d, start):
    global t
    if d == m:
        for tt in t:
            print(tt+1, end=' ')
        print()
    else:
        for i in range(n):
            if not visited[i]:
                visited[i] = 1
                t.append(i)
                solve(d+1, i)
                t.pop()
                visited[i] = 0

visited = [0 for i in range(n)]
t = []
solve(0, 0)

