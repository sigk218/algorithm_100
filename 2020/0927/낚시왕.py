import sys
sys.stdin = open('input.txt', 'r')

def move(arr):

    new_arr = [[[0, 0, 0] for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            # 상어가 있다면 이동한다.
            if arr[i][j][2] == 0: continue
            # i, j 로 하면 다음 루프에서 값이 변경 된다!
            ni, nj = i, j
            (s, d, z) = arr[ni][nj]
            for _ in range(s):
                ni += direction[d][0]
                nj += direction[d][1]
                if ni < 0 or ni >= r or nj < 0 or nj >= c:
                    # ######### 여기서도 방향 ㅠㅠ
                    ni -= direction[d][0]
                    nj -= direction[d][1]
                    if d == 0:
                        d = 1
                    elif d == 1:
                        d = 0
                    elif d == 2:
                        d = 3
                    else:
                        d = 2
                    ni += direction[d][0]
                    nj += direction[d][1]
            # 크기 비교 해야하므로 z
            if new_arr[ni][nj][2] < z:
                new_arr[ni][nj] = [s, d, z]
    return new_arr


r, c, m = map(int, input().split())
arr = [[[0, 0, 0] for _ in range(c)] for _ in range(r)]

for _ in range(m):
    i, j, s, d, z = map(int, input().split())
    # 속력, 이동 방향, 크기
    arr[i-1][j-1] = [s, d-1, z]

direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]

# 낚시왕이 잡은 상어 크기의 합
total = 0
# print(*arr, sep='\n')
for j in range(c):
    # 낚시왕이 오른쪽으로 한 칸
    for i in range(r):
        # 제일 가까이 있는 것을 잡는다
        if arr[i][j][2]:
            total += arr[i][j][2]
            # print(arr[i][j])
            arr[i][j] = [0, 0, 0]
            break
        # 상어가 이동한다
    temp = move(arr)
    arr = temp
print(total)



