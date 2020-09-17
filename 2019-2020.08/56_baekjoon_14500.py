import sys
sys.stdin = open('input.txt', 'r')

# 테르노미노는 모양이 고정
# 회전(오른쪽 90, 180, 270), 대칭(상하, 좌우) 가능
# 테르노미노는 하나만 놓는다

# 1. 테르노미노 모양 만들기
tr1 = [[1, 1, 1, 1]]
tr2 = [[1],[1],[1],[1]]
tr3 = [[1, 1],
       [1, 1]]
tr4 = [[1, 0, 0],
       [1, 0, 0],
       [1, 1, 0]]
tr5 = [[0, 0, 1],
       [0, 0, 1],
       [0, 1, 1]]
tr6 = [[1, 0, 0],
       [1, 1, 1]]
tr7 = [[0, 0, 1],
       [1, 1, 1]]
tr8 = [[1, 1],
       [0, 1],
       [0, 1]]
tr9 = [[1, 1],
       [1, 0],
       [1, 0]]
tr10 = [[1, 1, 1],
        [1, 0, 0]]
tr11 = [[1, 1, 1],
        [0, 0, 1]]
tr12 = [[1, 0],
       [1, 1],
       [0, 1]]
tr13 = [[0, 1],
        [1, 1],
        [1, 0]]
tr14 = [[0, 1, 1],
        [1, 1, 0]]
tr15 = [[1, 1, 0],
        [0, 1, 1]]
tr16 = [[1, 1, 1],
       [0, 1, 0]]
tr17 = [[0, 1, 0],
       [1, 1, 1]]
tr18 = [[0, 1],
        [1, 1],
        [0, 1]]
tr19 = [[1, 0],
        [1, 1],
        [1, 0]]

# 3. (i, j) 삐져나가지 않도록, 모든 경우의 수를 구하기, tr2는 한번만 하면 된다
def solve(li, type):
    global answer
    n, m = len(li), len(li[0])
    for i in range(n):
        for j in range(m):
            mysum = 0
            for si in range(len(type)):
                for sj in range(len(type[si])):
                    if type[si][sj] == 0:continue
                    if 0 <= si + i < n and 0 <= sj + j < m:
                        mysum += li[si+i][sj+j]
                    else:
                        mysum = -1
                        break
                if mysum == -1:
                    mysum = 0
                    break
            # print(mysum)
            answer = max(answer, mysum)


# 4. 합의 최대값 구하기
n, m = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]
trs = [tr1, tr2, tr3, tr4, tr5, tr6, tr7, tr8, tr9, tr10, tr11, tr12, tr13, tr14, tr15, tr16, tr17, tr18, tr19]

answer = 0
for tr in trs:
    solve(li, tr)
print(answer)
