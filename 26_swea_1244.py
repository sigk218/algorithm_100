import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(T):

    numbers, iter = input().split()
    iter = int(iter)
    numbers = list(numbers)
    numbers_len = len(numbers)

    answer = 0

    def dfs(temp, depth, now):
        global answer

        if depth == iter:
            answer = max(int(temp), answer)
        else:
            for pick1 in range(now, numbers_len-1):
                for pick2 in range(pick1+1, numbers_len):
                    temp = list(temp)
                    if temp[pick1] <= temp[pick2]:
                        temp[pick1], temp[pick2] = temp[pick2], temp[pick1]
                        dfs(''.join(temp), depth+1, pick1)
                        temp[pick1], temp[pick2] = temp[pick2], temp[pick1]


    dfs(numbers, 0, 0)
    print('#{} {}'.format(tc+1, answer))

