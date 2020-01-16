import sys
sys.stdin = open('input.txt', 'r')

T = 10
for tc in range(T):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    answer = 0
    right, left = 0, 0

    for i in range(100):
        col = 0
        answer = max(sum(arr[i]), answer)
        right += arr[i][i]
        left += arr[n - 1 - i][n - 1 - i]
        for j in range(100):
            col += arr[j][i]
        answer = max(col, answer)

    answer = max(right, answer)
    answer = max(left, answer)
    print('#{} {}'.format(tc+1, answer))