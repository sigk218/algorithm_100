import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(T):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    def go(x, y, d1, d2):

        # 똑같은 디저트를 먹었는 지, 안 먹었는 지
        visited = [0 for _ in range(101)]
        visited[arr[x][y]] = 1
        for di in range(1, d1+1):
            if visited[arr[x+di][y-di]]: return -1
            visited[arr[x + di][y - di]] = 1
            if visited[arr[x+d2+di][y+d2-di]]: return -1
            visited[arr[x + d2 + di][y + d2 - di]] = 1

            # print('1', x+di, y-di)
            # print('2', x+d2+di, y+d2-di)
        for di in range(1, d2+1):
            if visited[arr[x+di][y+di]]: return -1
            visited[arr[x + di][y + di]] = 1
            # 마지막 하나는 겹친다.
            if di == d2: break
            if visited[arr[x+d1+di][y-d1+di]]: return -1
            visited[arr[x + d1 + di][y - d1 + di]] = 1
            # print('3', x+di, y+di)
            # print('4', x+d1+di, y-d1+di)
        if sum(visited) == 3:
            print(x, y, d1, d2)
            print(visited)
        return sum(visited)

    answer = 0
    for d1 in range(1, n):
        for d2 in range(1, n):
            for x in range(n-1):
                for y in range(1, n-1):
                    if y-d1 < 0 or x + d1 + d2 >= n or y + d2 >= n: continue
                    # print(go(x, y, d1, d2))
                    if answer == 0:
                        answer = go(x, y, d1, d2)
                    else:
                        answer = max(answer, go(x, y, d1, d2))
    print('#{} {}'.format(tc+1, answer))