import sys
sys.stdin = open('input.txt', 'r')

def solve():
    global answer

    for start in range(1, n-1):
        for end in range(start, n-1):
            temp = 0
            # W
            for i in range(1, start):
                temp += color_cnt[i][0]
                temp += color_cnt[i][1]

            # B
            for i in range(start, end+1):
                temp += color_cnt[i][0]
                temp += color_cnt[i][2]

            # R
            for i in range(end+1, n-1):
                temp += color_cnt[i][1]
                temp += color_cnt[i][2]

            answer = min(temp, answer)


T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    flag = [input() for _ in range(n)]
    answer = 2501
    # r, b, w
    color_cnt = [[0] * 3 for _ in range(n)]

    for nn in range(n):
        color_cnt[nn][0] = flag[nn].count('R')
        color_cnt[nn][1] = flag[nn].count('B')
        color_cnt[nn][2] = flag[nn].count('W')

    solve()
    print('#{} {}'.format(tc+1, answer+color_cnt[0][0]+color_cnt[0][1]+color_cnt[n-1][1]+color_cnt[n-1][2]))




