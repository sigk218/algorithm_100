import sys
sys.stdin = open('input.txt' ,'r')

T= int(input())
for tc in range(T):
    arr = [list(map(int, input().split())) for _ in range(4)]

    def solve(i ,j):

        if len(temp) > 6:
            temp_str = ''.join(map(str, temp))
            answer.add(temp_str)
            return

        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            xx = i + dx
            yy = j + dy
            if 0 <= xx < 4 and 0 <= yy < 4:
                temp.append(arr[xx][yy])
                solve(xx, yy)
                temp.pop()

    answer = set()
    for i in range(4):
        for j in range(4):
            temp = []
            temp.append(arr[i][j])
            solve(i, j)
    print('#{} {}'.format(tc+1, len(answer)))