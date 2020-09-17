import sys
sys.stdin = open('input.txt', 'r')


def makeline(line):
    # 복원을 위해 copy
    newline = line[:]
    temp = []
    while newline:
        if len(newline) > 1 and newline[0] == newline[1]:
            temp.append(newline.pop(0) + newline.pop(0))
        else:
            temp.append(newline.pop(0))
    return temp


def rotate(direction, board):
    copy_board = [[0] * n for _ in range(n)]
    # 왼 쪽
    if direction == 0:
        for i in range(n):
            t = []
            for j in range(n):
                if board[i][j] != 0:
                    t.append(board[i][j])
            temp = makeline(t)
            for j in range(len(temp)):
                copy_board[i][j] = temp.pop(0)

    # 오른 쪽
    elif direction == 1:
        for i in range(n):
            t = []
            for j in range(n - 1, -1, -1):
                if board[i][j] != 0:
                    t.append(board[i][j])
            temp = makeline(t)
            for j in range(len(temp)):
                copy_board[i][n - 1 - j] = temp.pop(0)
    # 위
    elif direction == 2:
        for j in range(n):
            t = []
            for i in range(n):
                if board[i][j] != 0:
                    t.append(board[i][j])
            temp = makeline(t)
            for i in range(len(temp)):
                copy_board[i][j] = temp.pop(0)
        # print(*copy_board, sep='\n')
    # 아래
    elif direction == 3:
        for j in range(n):
            t = []
            for i in range(n - 1, -1, -1):
                if board[i][j] != 0:
                    t.append(board[i][j])
            temp = makeline(t)
            for i in range(len(temp)):
                copy_board[n - 1 - i][j] = temp.pop(0)

    return copy_board


# 최대 5번 이동시켜서 얻을 수 있는 가장 큰 블록을 출력한다.
# 어떻게 5번을 뽑을 것인지 ? 4방향중에 중복순열로 5개를 뽑아야 함으로 4** 5
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]


def solve(d, direction, tempboard):
    global cnt, answer
    # print(*tempboard, direction, d, sep='\n')
    answer = max(answer, max(sum(tempboard, [])))
    if d == 5:
        return
    else:
        for i in range(4):
            # 돌렸는데 이전과 같으면 멈추기
            # if rotate(direction, tempboard) == tempboard: return
            if rotate(i, tempboard) == tempboard: continue
            solve(d + 1, i, rotate(i, tempboard))


cnt = 0
answer = 0
solve(0, 0, board)
print(answer)
