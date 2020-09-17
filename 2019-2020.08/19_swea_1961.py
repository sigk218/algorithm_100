import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(T):
    print('#{}'.format(tc+1))
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    def rotate_90():
        new_arr = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                new_arr[j][n- 1 - i] = arr[i][j]
        return new_arr

    def rotate_180():
        new_arr = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                new_arr[n-1-i][n-1-j] = arr[i][j]
        return new_arr

    def rotate_270():
        new_arr = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                new_arr[n-1-j][i] = arr[i][j]
        return new_arr

    a90 = rotate_90()
    a180 = rotate_180()
    a270 = rotate_270()
    for nn in range(n):
        print(''.join(map(str, a90[nn]))+' '
              +''.join(map(str, a180[nn]))+' '
              +''.join(map(str, a270[nn])))


