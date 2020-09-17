import sys
sys.stdin = open('input.txt', 'r')

# 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다
# 맨 처음 뱀은 맨 좌측, 길이는 1, 오른쪽을 향한다
# 머리를 다음칸에 위치시킨다
# 사과가 있다면 -> 몸길이 늘린다, 사과가 없다면 -> 이동만 한다

def inbox(x, y):
    if 0 <= x < n and 0 <= y < n : return True
    else:
        return False
n = int(input())
arr = [[-1 for _ in range(n)] for _ in range(n)]

# +1 은 오른쪽, +3 은 왼쪽
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]


for apple in range(int(input())):
    i, j = map(int, input().split())
    # 사과는 -2
    arr[i-1][j-1] = -2
move = dict()
for _ in range(int(input())):
    sec, d = input().split()
    move[int(sec)] = d

r, c, d = 0, 0, 0
arr[r][c] = 0
snake = 1
second = 0

while second <= 10000:

    if move.get(second):
        # 왼쪽이라면
        if move[second] == 'L':
            d = (d + 3) % 4
        else:
            d = (d + 1) % 4
    r += direction[d][0]
    c += direction[d][1]
    if not inbox(r, c):
        break
    # 사과가 있다면
    if arr[r][c] == -2:
        snake += 1
    # 내 몸통을 만난 경우
    elif arr[r][c] != -1 and second - arr[r][c] <= snake:
        break
    arr[r][c] = second
    second += 1
print(second+1)