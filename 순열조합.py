# 순열
def perm(k):
    global N
    if k == N:
        print(t)
    else:
        for i in range(N):
            if visited[i]:
                continue
            t[k] = l[i]
            visited[i] = 1
            perm(k+1)
            visited[i] = 0

l = [0, 1, 2]
N = 3
t = [0] * N
visited = [0]*N
perm(0)


def powerset(k):
    if k == N:
        for i in range(k):
            if a[i]:
                print(l[i], end=' ')
        print()
    else:
        a[k] = 1
        powerset(k+1)
        a[k] = 0
        powerset(k+1)
a = [0]*N
powerset(0)