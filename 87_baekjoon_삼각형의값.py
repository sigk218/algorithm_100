import sys
sys.stdin = open('input.txt', 'r')

def solve(x, y, nn):
    tempsum = 0
    if not (0 <= x + nn < n and 0 <= y + nn < 2*(n-1)+1): return 0
    for ni in range(nn+1):
        for j in range(2*ni+1):
            tempsum += arr[x+ni][y+j]
            # print(arr[x+ni][y+j], end=' ')
        # print()
    return tempsum

while True:
    T = 1
    myinput = input()
    if myinput == '0':break
    myinput = list(map(int, myinput.split()))
    n = myinput[0]
    myinput = myinput[1:]
    arr = [[0 for _ in range(2*(n-1)+1)] for __ in range(n)]

    idx = 0
    for i in range(n):
        for j in range(2*i+1):
            arr[i][j] = myinput[idx]
            idx += 1

    answer = 0
    for i in range(n):
        for j in range(2*i+1):
            for nn in range(n):
                answer = max(solve(i, j, nn), answer)
    print('{}. {}'.format(T, answer))
    T += 1

