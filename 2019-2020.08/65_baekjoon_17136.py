import sys
sys.stdin = open('input.txt', 'r')

# 1X1 ~ 5X5 각 5장씩
# 보드는 10X10
# 1이 적힌 칸은 모두 색종이로 덮여져있어야함
# 밖으로 나가면 x, 겹쳐도 X , 0이 적힌 칸에는 색종이 X
# 1이 적힌 모든 칸을 붙이는데 필요한 색종이의 최소 개수
# 참고: https://jaimemin.tistory.com/1249

def solve(x, y, cnt):
    global answer
    # 가지치기
    if answer <= cnt: return

    if x == 10:
        answer = min(answer, cnt)
        return

    if y == 10:
        solve(x+1, 0, cnt)
        return

    if board[x][y] == 0:
        solve(x, y+1, cnt)

    for size in range(5, 0, -1):
        if paper[size] == 0 or x+size > 10 or y+size > 10: continue
        temp = [(x, y)]
        flag = True
        for i in range(size):
            for j in range(size):
                xx = x + i
                yy = y + j
                temp.append((xx, yy))
                if board[xx][yy] == 0:
                    flag = False
                    break
            if flag == False:
                break
        if flag:
            if paper[size]:
                paper[size] -= 1
                for ii, jj in temp:
                    board[ii][jj] = 0
                solve(x, jj+1, cnt+1)
                paper[size] += 1
                for ii, jj in temp:
                    board[ii][jj] = 1


board = list(list(map(int, input().split())) for _ in range(10))
paper = [0, 5, 5, 5, 5, 5]
answer = 100000000
solve(0, 0, 0)
print(answer if answer != 100000000 else -1)