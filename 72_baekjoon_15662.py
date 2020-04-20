import sys
sys.stdin = open('input.txt', 'r')

# 톱니 8개, 총 T개
# 회전은 시계, 반시계
# 톱니바퀴가 회전 할 때, 서로 맞닿은 극에 따라 옆에있는 톱니
# 회전하거나, 안하거나 
# 한번에 검사한 후 회전

T = int(input())
arr = [list(map(int, input())) for _ in range(T)]
k = int(input())
for _ in range(k):
    number, direction = map(int, input().split())
    number -= 1
    # 회전할 톱니 바퀴의 방향
    d = [0 for I in range(T)]
    d[number] = direction
    # 나보다 작은 경우
    for i in range(number-1, -1, -1):
        if arr[i][2] != arr[i+1][6]:
            d[i] = -d[i+1]
        else:
            break
    # 나보다 큰 경우
    for i in range(number+1, T):
        if arr[i][6] != arr[i-1][2]:
            d[i] = -d[i-1]
        else:
            break
    for i in range(T):
        if d[i] == 0: continue
        # 시계방향
        elif d[i] == 1:
            temp = arr[i][7]
            for j in range(7, 0, -1):
                arr[i][j] = arr[i][j-1]
            arr[i][0] = temp
        # 반 시계 방향
        else:
            temp = arr[i][0]
            for j in range(7):
                arr[i][j] = arr[i][j+1]
            arr[i][7] = temp
total = 0
for i in range(T):
    if arr[i][0]:
        total += 1
print(total)