def solution(board, moves):
    answer = 0
    q = []
    for m in moves:
        # print(*board, sep='\n')
        for i in range(len(board)):
            if board[i][m-1]:
                q.append((board[i][m-1]))
                board[i][m-1] = 0
                break

        if len(q) > 1:
            d1 = q.pop()
            d2 = q.pop()
            if d1 == d2:
                answer += 2
            else:
                q.append(d2)
                q.append(d1)
        # print(m, q)


    return answer


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board, moves))