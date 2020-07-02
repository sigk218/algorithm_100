import sys
sys.stdin = open('input.txt', 'r')

# 최대 5번 이동해서 만들 수 있는 가장 큰 블록
# 움직이는 것
# 움직이는 방향을 뽑는 것(순열 5! = 120)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
# print(*board, sep='\n')

import collections
def move(mylist):
    fakemylist = mylist[:]
    result = collections.deque()
    while fakemylist:
        if len(fakemylist) > 1 and fakemylist[-1] == fakemylist[-2]:
            result.appendleft(fakemylist.pop() + fakemylist.pop())
        else:
            result.appendleft(fakemylist.pop())
    return result

def rotate(d, board):
    # print(board)
    new_board = [[0 for _ in range(n)] for _ in range(n)]
    # 오른쪽
    if d == 0:
       for i in range(n):
           t = []
           for j in range(n):
               if board[i][j]:
                   t.append(board[i][j])
           temp = move(t)
           for j in range(n-1, -1, -1):
               if temp:
                   new_board[i][j] = temp.pop()
               else:
                   break
    # 왼쪽
    elif d == 1:
        for i in range(n):
            t = []
            for j in range(n-1, -1, -1):
                if board[i][j]:
                    t.append((board[i][j]))
            temp = move(t)
            for j in range(n):
                if temp:
                    new_board[i][j] = temp.pop()
                else:
                    break
    # 위쪽
    elif d == 2:
        for i in range(n):
            t = []
            for j in range(n-1, -1, -1):
                if board[j][i]:
                    t.append(board[j][i])
            temp = move(t)
            for j in range(n):
                if temp:
                    new_board[j][i] = temp.pop()
                else:
                    break
    # 아래쪽
    else:
        for i in range(n):
            t = []
            for j in range(n):
                if board[j][n-i-1]:
                    t.append(board[j][n-i-1])
            # print(t)
            temp = move(t)
            # print(temp)
            for j in range(n-1, -1, -1):
                if temp:
                    new_board[j][n-1-i] = temp.pop()
                else:
                    break
    return new_board

answer = 0
# 다섯가지 경우 뽑기
for a in range(4):
    Aboard = rotate(a, board)
    answer = max(answer, max(sum(Aboard, [])))
    for b in range(4):
        Bboard = rotate(b, Aboard)
        answer = max(answer, max(sum(Bboard, [])))
        if Aboard == Bboard: continue
        for c in range(4):
            Cboard = rotate(c, Bboard)
            answer = max(answer, max(sum(Cboard, [])))
            # if Bboard == Cboard: continue
            for d in range(4):
                Dboard = rotate(d, Cboard)
                answer = max(answer, max(sum(Dboard, [])))
                # if Cboard == Dboard: continue
                for e in range(4):
                    Eboard = rotate(e, Dboard)
                    answer = max(answer, max(sum(Eboard, [])))
# solve(0, board)
# print(*rotate(3, board), sep='\n')
print(answer)



