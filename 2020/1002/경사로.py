import sys
sys.stdin = open('input.txt', 'r')

# 한 줄에 대해서 경사로를 놓을 수 있는지 검사
def check(line):

    visited = [0 for _ in range(n)]
    idx = 1
    while idx < n:
        # print(line[idx-1], line[idx])
        if line[idx-1] == line[idx]:
            idx += 1
            continue
        elif abs(line[idx-1] - line[idx]) > 1:
            return False

        # 현재가 높은 이라면 ?
        elif line[idx-1] + 1 == line[idx]:
            if idx - 1 - (l - 1) < 0: return False
            if visited[idx-1] : return  False
            visited[idx-1] = 1
            for li in range(1, l):
                if visited[idx - 1 - li]: return False
                visited[idx - 1 - li] = 1
                if line[idx-1] != line[idx-1-li]:
                    return False

        # 현채 칸이 낮은 이라면 ?
        elif line[idx-1] == line[idx] +1:
            if idx + l > n: return False
            if visited[idx]: return False
            visited[idx] = 1
            for li in range(1, l):
                if visited[idx+li]:return False
                visited[idx+li] =1
                if line[idx] != line[idx+li]:
                    return False
            else:
                idx += l - 1
        idx += 1
    return True


n, l = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]

answer = 0
for i in range(n):
    temp = []
    if check(arr[i]):
        answer += 1
    for j in range(n):
        temp.append(arr[j][i])
    if check(temp):
        answer += 1
print(answer)

