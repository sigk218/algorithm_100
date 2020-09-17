import sys
sys.stdin = open('input.txt', 'r')

# 전체 맵은 n * m
# 청소기 : 위치, 방향

def inbox(x, y):
    if 0 <= x < n and 0 <= y < m:
        return True
    else:            
        return False

# 북, 동, 남, 서
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

n, m = map(int, input().split())
r, c, d = map(int, input().split())

# 빈칸은 0, 벽은 1
mymap = [list(map(int, input().split())) for _ in range(n)]

answer = 0
while inbox(r, c):
    # print(r, c)
    # 현재 칸을 청소한다 -1로 표시
    if mymap[r][c] == 0:
        mymap[r][c] = 2
        answer += 1
    # 네 방향이 모두 청소가 되어있는 경우
    isclean = True
    for i in range(4):
        if not inbox(r + direction[i][0], c + direction[i][1]) or not(mymap[r + direction[i][0]][c + direction[i][1]] != 0):
            isclean = False
            break
    if isclean:
        # 후진가능하면 후진하고
        nr, nc = r - direction[d][0], c - direction[d][1]
        if inbox(nr, nc) and mymap[nr][nc] == 1:
            break
        else:
            r, c = nr, nc
    else:
        d = (d + 3) % 4
        nr, nc = r + direction[d][0], c + direction[d][1]
        if inbox(nr, nc) and mymap[nr][nc] == 0:
            r, c = nr, nc
print(answer)