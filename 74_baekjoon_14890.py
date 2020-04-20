import sys
sys.stdin = open('input.txt', 'r')

n, l = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def check(temp):
    visited = [0 for _ in range(n)]
    for i in range(1, n):
        if temp[i-1] != temp[i]:
            dif = temp[i-1] - temp[i]
            if dif > 1: return False
            elif dif == -1:
                # 벽을 나갈 경우
                if i-1-(l-1) < 0: return False
                for ll in range(l):
                    if temp[i-1] != temp[i-1-ll]:
                        return False
                    if visited[i-1-ll]:
                        return False
                    else:
                        visited[i-1-ll] = 1
            else:
                if i + l -1 >= n: return False
                for ll in range(l):
                    if temp[i] != temp[i+ll]:
                        return False
                    if visited[i+ll]:
                        return False
                    else:
                        visited[i+ll] = 1
    return True

cnt = 0
for i in range(n):
    if check(arr[i]):
        # print(li[i])
        cnt += 1
    t = []
    for j in range(n):
        t.append(arr[j][i])
    if check(t):
        # print(t)
        cnt += 1
print(cnt)