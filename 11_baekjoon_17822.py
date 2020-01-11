import sys
sys.stdin = open('input.txt', 'r')

def rotat(x, d, k):
    onepan_copy = [[0] * m for _ in range(n)]

    # 시계 방향
    if d == 0:
        for i in range(n):
            for j in range(m):
                if (i + 1) % x == 0:
                    onepan_copy[i][j] = onepan[i][((j-k) + m) % m]
                    continue
                onepan_copy[i][j] = onepan[i][j]

    # 반시계 방향
    if d == 1:
        for i in range(n):
            for j in range(m):
                if (i + 1) % x == 0:
                    onepan_copy[i][j] = onepan[i][(j+k) % m]
                    continue
                onepan_copy[i][j] = onepan[i][j]
    return onepan_copy

def findnearnum():
    visited = [[0] * m for _ in range(n)]
    answer = set()
    for i in range(n):
        for j in range(m):
            if onepan[i][j] == 0: continue
            if not visited[i][j]:
                for di, dj in (0, 1), (1, 0), (-1, 0), (0, -1):
                    ii = i + di
                    jj = (j + dj + m) % m
                    if 0 <= ii < n and 0 <= jj < m:
                        if onepan[i][j] == onepan[ii][jj]:
                            visited[ii][jj] = 1
                            answer.add((i, j))
                            answer.add((ii, jj))
    return answer
# 인접하면서 수가 같은 것을 찾기
# 같은 수가 있다면 - > 모두 지운다
# 없다면 평균을 구하고, 평균보다 큰 수는 -1, 작은수 + 1
# 인접: 상, 하, 좌, 우 인접에 처음이랑 끝도 인접

n, m, t = map(int, input().split())

onepan = [list(map(int, input().split())) for _ in range(n)]
xdks = [list(map(int, input().split())) for _ in range(t)]

for x, d, k in xdks:
    onepan = rotat(x, d, k)
    # print(onepan)
    answer = findnearnum()
    # print(answer)

    if answer:
        for i, j in answer:
            onepan[i][j] = 0
    else:
        cnt = 0
        total = 0
        for i in range(n):
            for j in range(m):
                if onepan[i][j] == 0: continue
                cnt += 1
                total += onepan[i][j]
        if cnt == 0:
            avg = 0
        else:
            avg = total / cnt
        if avg:
            for i in range(n):
                for j in range(m):
                    if onepan[i][j] == 0: continue
                    if onepan[i][j] > avg:
                        onepan[i][j] -= 1
                    elif onepan[i][j] < avg:
                        onepan[i][j] += 1

print(sum(sum(onepan, [])))

