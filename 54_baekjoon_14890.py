import sys
sys.stdin = open('input.txt' ,'r')

def solve(line):
    visited = [0] * n
    for i in range(1, n):
        diff = line[i-1] - line[i]
        temp = []
        if diff == 0:continue
        elif abs(diff) >= 2: return False
        elif diff == 1:
            temp.append(i)
            for j in range(1, l):
                if i+j >= n: return False
                temp.append(i+j)
                if line[i] != line[i+j]: return False
        elif diff == -1:
            temp.append(i-1)
            for j in range(1, l):
                if i - j - 1 < 0 : return False
                temp.append(i-j-1)
                if line[i-1] != line[i-1-j]: return False
        # if len(temp) > 1:
        # print(line[temp[0]], temp)
        for t in temp:
            if visited[t]: return False
            visited[t] = 1
    return True



n, l = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]

# print(solve([3, 2, 2, 1, 2, 3]))
cnt = 0
for i in range(n):
    if solve(li[i]):
        # print(li[i])
        cnt += 1
    t = []
    for j in range(n):
        t.append(li[j][i])
    if solve(t):
        # print(t)
        cnt += 1
print(cnt)