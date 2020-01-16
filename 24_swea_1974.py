import sys
sys.stdin = open('input.txt', 'r')

def rowcheck():
    for i in range(9):
        row_cnt = [0] * 10
        for j in range(9):
            row_cnt[sudoku[i][j]] = 1
        if sum(row_cnt) != 9:
            return False
    return True

def colcheck():
    for j in range(9):
        col_cnt = [0] * 10
        for i in range(9):
            col_cnt[sudoku[i][j]] = 1
        if sum(col_cnt) != 9:
            return False
    return True

def minicheck():
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            mini_cnt = [0] * 10
            for di in range(3):
                for dj in range(3):
                    mini_cnt[sudoku[i+di][j+dj]] = 1
            if sum(mini_cnt) != 9:
                return False
    return True

T = int(input())
for tc in range(T):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    flag = 0
    if rowcheck():
        if colcheck():
            if minicheck():
                flag = 1
    print('#{} {}'.format(tc+1, 1 if flag else '0'))


