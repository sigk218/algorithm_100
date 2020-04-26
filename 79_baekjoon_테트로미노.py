import sys
sys.stdin = open('input.txt', 'r')


def findT(x, y, cnt, currnet_sum):
    global answer

    if cnt > 3 : return
    if cnt == 3:
        answer = max(answer, currnet_sum)
        return
    for dx, dy in (0, 1), (1, 0), (-1, 0), (0, -1):
        xx = x + dx
        yy = y + dy
        if 0 <= xx < n and 0 <= yy < m and not visited[xx][yy]:
            visited[xx][yy] = 1
            findT(xx, yy, cnt+1, currnet_sum+arr[xx][yy])
            visited[xx][yy] = 0

n, m = map(int, input().split())
arr =[list(map(int, input().split())) for _ in range(n)]
# 3칸을 연속해서 방문 한다

visited = [[0 for _ in range(m)] for _ in range(n)]
answer = 0
for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        findT(i, j, 0, arr[i][j])
        visited[i][j] = 0
        if j+2 < m:
            temp = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            if i-1 >= 0:
                answer = max(answer, temp+arr[i-1][j+1])
            if i+1 < n:
                answer = max(answer, temp+arr[i+1][j+1])
        if i+2 < n:
            temp = arr[i][j] + arr[i+1][j] + arr[i+2][j]
            if j+1 < m:
                answer = max(answer, temp+arr[i+1][j+1])
            if j-1 >= 0:
                answer = max(answer, temp+arr[i+1][j-1])
print(answer)



