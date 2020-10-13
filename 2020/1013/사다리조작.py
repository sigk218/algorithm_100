import sys
sys.stdin = open('input.txt', 'r')

# 사다리에 가로선을 추가해서
# 추가해야하는 가로선의 최솟값
# 만약 정답이 3보다 큰 값이면 -1을 출력한다

def check():
    # i번 세로선의 결과가 i인지
    for j in range(n):
        start = j
        i = 0
        while i < h:
            if start == 0 and arr[i][start]:
                start += 1
            elif arr[i][start]:
                start += 1
            elif arr[i][start-1]:
                start -= 1
            i += 1
        if start != j:
            return False
    return True

def pick(d, sx, sy):
    global answer

    if d >= answer:
        return

    if check():
        answer = min(answer, d)

    if d == 3:
        return

    for i in range(sx, h):
        sy = sy if i == sx else 0
        for j in range(sy, n-1):
            if arr[i][j]: continue
            # 두 가로선이 연속하거나, 서로 접하면 안된다
            if j == 0 and arr[i][j] == 0 and arr[i][j+1] == 0:
                arr[i][j] = 1
                pick(d+1, i, j)
                arr[i][j] = 0
            elif j == n-2 and arr[i][j] == 0 and arr[i][j-1] == 0:
                arr[i][j] = 1
                pick(d + 1, i, j)
                arr[i][j] = 0
            elif arr[i][j] == 0 and arr[i][j-1] == 0 and arr[i][j+1] == 0:
                arr[i][j] = 1
                pick(d + 1, i, j)
                arr[i][j] = 0

n, m, h = map(int, input().split())

# 가로선 추가한다
# i번의 결과가 i번인지 체크한다
arr = [[0 for _ in range(n)] for _ in range(h)]

for _ in range(m):
    x, y = map(int, input().split())
    arr[x-1][y-1] = 1
# print(*arr, sep='\n')

answer = 4
pick(0, 0, 0)
print(answer if answer < 4 else -1)

# i, j 헷갈림 
# 두 자리수에서 조합 뽑기 -> 좌표 헷갈림