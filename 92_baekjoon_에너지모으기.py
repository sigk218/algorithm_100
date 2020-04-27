import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
arr = list(map(int, input().split()))

def dfs(d, score):
    global answer
    # print(d, score)
    if d == n - 2:
        # print('도착입니댜')
        answer = max(answer, score)
        return
    else:
        for i in range(1, n-1):
            if visited[i] == 0:

                visited[i] = 1
                for j1 in range(i-1,-1,-1):
                    if visited[j1]:
                        break
                for j2 in range(i+1, n):
                    if visited[j2]:
                        break
                # print(i, j1, j2, arr[i], arr[j1], arr[j2])
                dfs(d+1, score+(arr[j1]*arr[j2]))
                visited[i] = 0

visited = [0 for _ in range(n)]
answer = 0
dfs(0, 0)
print(answer)