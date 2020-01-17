import sys
sys.stdin = open('input.txt', 'r')
import collections

# 오른쪽(0), 아래(1), 왼쪽(2), 위(3)
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def solve(ix, iy, iidx, itemp):
    global flag

    q = collections.deque()
    q.append((ix, iy, iidx, itemp))

    while q:
        x, y, idx, temp = q.pop()
        # print(x, y, idx, temp, huk_map[x][y])
        if visited.get((x, y, idx, temp)) == None:
            visited[(x, y, idx, temp)] = 1
            if huk_map[x][y] == '@':
                flag = True
                return
            elif huk_map[x][y] == '?':
                for i in range(4):
                    # print((x + directions[i][0] + r) % r, (y + directions[i][1] + c) % c, i, temp)
                    q.append(((x + directions[i][0] + r) % r, (y + directions[i][1] + c) % c, i, temp))
            else:
                if huk_map[x][y] == '<':
                    idx = 2
                elif huk_map[x][y] == '>':
                    idx = 0
                elif huk_map[x][y] == '^':
                    idx = 3
                elif huk_map[x][y] == 'v':
                    idx = 1
                elif huk_map[x][y] == '_':
                    if temp == 0:
                        idx = 0
                    else:
                        idx = 2
                elif huk_map[x][y] == '|':
                    if temp == 0:
                        idx = 1
                    else:
                        idx = 3
                elif huk_map[x][y].isdecimal() and 0 <= int(huk_map[x][y]) < 10:
                        temp = int(huk_map[x][y])
                elif huk_map[x][y] == '+':
                    if temp == 15:
                        temp = 0
                    else:
                        temp += 1
                elif huk_map[x][y] == '-':
                    if temp == 0:
                        temp = 15
                    else:
                        temp -= 1
                # if huk_map[x][y] == '.':
                #     pass
                q.append(((x + directions[idx][0] + r) % r, (y + directions[idx][1] + c) % c, idx, temp))


T = int(input())
for tc in range(T):
    r, c = map(int, input().split())
    huk_map = [list(input()) for _ in range(r)]
    visited = dict()
    flag = False
    solve(0, 0, 0, 0)
    print('#{} {}'.format(tc+1, 'YES' if flag else 'NO'))