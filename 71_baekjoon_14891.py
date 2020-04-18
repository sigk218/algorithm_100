import sys, collections
sys.stdin = open('input.txt', 'r')
# 8개의 톱니가 4개
# K 번 회전시킨다
# 시계방향 회전, 반 시계방향 회전
def rotate(arr_temp, direction):
    new_arr_temp = collections.deque(arr_temp)
    # 시계 방향
    if direction == 1:
        last = new_arr_temp.pop()
        new_arr_temp.appendleft(last)
    else:
        first = new_arr_temp.popleft()
        new_arr_temp.append(first)
    # print(temp, direction, new_arr_temp)
    return list(new_arr_temp)

# 방향이 다를때만 회전

# n극은 0, s극은 1로 나타남
arr = [list(map(int, input())) for _ in range(4)]
for kk in range(int(input())):
    number, origin = map(int, input().split())
    number -= 1
    # print(number, origin)
    # 확인 먼저 하고
    change_list = set()
    # 나보다 작은것들에 대해서
    temp = number
    compare = arr[number][6]
    direction = origin
    for _ in range(number):
        temp -= 1
        direction = 1 if direction == -1 else -1
        if compare == arr[temp][2]:
            break
        else:
            change_list.add((temp, direction))
            compare = arr[temp][6]
    temp = number
    compare = arr[number][2]
    direction = origin
    # 나보다 큰 것들에 대해서
    for _ in range(number+1, 4):
        temp += 1
        direction = 1 if direction == -1 else -1
        if compare == arr[temp][6]:
            break
        else:
            change_list.add((temp, direction))
            compare = arr[temp][2]

    change_list.add((number, origin))
    for t, d in change_list:
        arr[t] = rotate(arr[t], d)

total = 0
for i in range(4):
    if arr[i][0]:
        total += 2 ** (i)
print(total)
