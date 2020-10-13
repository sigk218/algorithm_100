import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(1, t+1):
    n = int(input())

    # 시간의 최대가 40001인가.. ?

    dir = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    atom = dict()
    for _ in range(n):
        x, y, d, e = map(int, input().split())
        atom[(2*x, 2*y)] = [d, e]

    answer = 0
    # 2001
    for _ in range(2001):

        new_atom = {}
        del_list = set()

        for (x, y), (d, e) in atom.items():
            nx, ny = x + dir[d][0], y + dir[d][1]
            # 2개 이상일 때만 지운다
            if new_atom.get((nx, ny)):
                del_list.add((nx, ny))
                new_atom[(nx, ny)].append(e)
            else:
                new_atom[(nx, ny)] = [d, e]



        for (x, y) in del_list:
            answer += sum(new_atom[(x, y)][1:])
            del new_atom[(x, y)]

        if new_atom == {}:
            break

        atom = new_atom

    print('#{} {}'.format(tc, answer))
