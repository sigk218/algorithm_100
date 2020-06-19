import sys
sys.stdin = open('input.txt', 'r')

'''
7
1 5 8 12 9 10 13 
'''
n = int(input())
arr = []
idx = 0
for i in range(n):
    temp = []
    for j in range(n):
        # 짝수 일 경우 1개가 적다
        if (i+1) % 2 == 0 and j == n-1:
            continue
        idx += 1
        first, second = map(int, input().split())
        # 현재 타일의 번호, 타일의 첫 번째 값, 두 번째 값
        temp.append([idx, first, second])
    arr.append(temp)
# print(*arr, sep='\n')


# 첫 줄의 가장 첫 타일에서 마지막 줄의 마지막 타일로 이동하는 가장 짧은 경로 
# 마지막으로 이동할 수 없는 경우, 번호가 가장 큰 타일로 이동

def inbox(x, y):
    if 0 <= x < n and 0 <= y < len(arr[x]):
        return True
    else:
        return False

# 한 타일에서 다른 타일로 넘어가려면, 같은 변을 공유하는 조각에 쓰여있는 숫자가
# 같아야 한다.
dx1 = [-1, 0, 1, 1, 0, -1]
dy1 = [1, 1, 1, 0, -1, 0]
dx2 = [-1, 0, 1, 1, 0, -1]
dy2 = [0, 1, 0, -1, -1, -1]
import collections
def bfs():
    global maxidx
    # a번은 b에서 부터 왔다
    path = [0 for _ in range(idx+1)]
    c = [[0 for _ in range(n)] for _ in range(n)]
    q = collections.deque()
    q.append((0, 0))
    # 시작점 체크 해주기
    c[0][0] = 1
    # 오른쪽인지 왼 쪽인지 중요하다.
    # 왼쪽이라면 왼쪽을 검사하고, 오른쪽이라면 오른쪽을 검사해야한다.. .. Aㅏ...

    while q:
        x, y = q.popleft()
        maxidx = max(maxidx, arr[x][y][0])
        if x % 2 == 1:
            dx, dy = dx1, dy1
        else:
            dx, dy = dx2, dy2
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            if inbox(nx, ny):
                if c[nx][ny] == 0:
                    if i <= 2:
                        if arr[x][y][2] == arr[nx][ny][1]:
                            c[nx][ny] = c[x][y] + 1
                            path[arr[nx][ny][0]] = arr[x][y][0]
                            q.append([nx, ny])
                    else:
                        if arr[x][y][1] == arr[nx][ny][2]:
                            c[nx][ny] = c[x][y] + 1
                            path[arr[nx][ny][0]] = arr[x][y][0]
                            q.append([nx, ny])
    # print(path)
    return path
maxidx = 1
find = bfs()
# print(find)

# 최댓 값 찾기, 마지막 타일에 도달하지 못했을 때
# for i in range(idx, 1, -1):
#     if find[i]:
#         maxidx = i
#         break
answer = [maxidx]
while find[maxidx] != 0:
    answer.append((find[maxidx]))
    maxidx = find[maxidx]
answer.reverse()
print(len(answer))
for a in answer:
    print(a, end=' ')
