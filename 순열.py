

# 순열
# n개 뽑아서 줄 세우기
def permi(d, N):
    global cnt

    if d == N:
        cnt += 1
        print(cnt, temp)
        return
    else:
        for i in range(N):
            if visited[i]: continue
            temp[d] = arr[i]
            visited[i] = 1
            permi(d+1, N)
            visited[i] = 0


N = 4
arr = [1, 2, 3, 4]
visited = [0 for _ in range(N)]
temp = [0 for _ in range(N)]
cnt = 0
permi(0, N)

