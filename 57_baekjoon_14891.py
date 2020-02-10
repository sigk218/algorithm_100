import sys
sys.stdin = open('input.txt', 'r')

# 1. 회전
def rotate(wheels, direction):
#  1-1. 시계
    new_wheels = [0] * 8
    if direction == -1:
        for i in range(8):
            new_wheels[i] = wheels[(i+1) % 8]

#  1-2. 반시계
    if direction == 1:
        for i in range(8):
            new_wheels[i] = wheels[(i-1+8) % 8]
    return new_wheels


# 2. 관계 (맞닿아있는 점)
def relation(wheel1, wheel2):
    # 맞닿은 극이 다르면 -> 이전 톱니바퀴의 반대 방향으로 회전
    if wheel1[2] != wheel2[6]:
        return True
    # 같은 극이면 -> 회전하지 않게 된다.
    else:
        return False


# 4. 총 k 번 회전 한다
wheel = [list(map(int, input())) for _ in range(4)]
# 회전 최대 100번, 회전은 한번에함
k = int(input())
commands = [list(map(int, input().split())) for _ in range(k)]
# 3. 1 ~ 나, 나~끝 두번의 루프가 돌아야한다.


for turn, direction in commands:
    change_list = [(turn-1, direction)]
    temp_d1 = direction
    for i in range(turn-1, 0, -1):
        temp = relation(wheel[i-1], wheel[i])
        if temp == False:
            break
        if temp_d1 == - 1:
            temp_d1 = 1
        else:
            temp_d1 = -1
        change_list.append((i-1, temp_d1))

    temp_d2 = direction
    for i in range(turn-1, 3):
        temp = relation(wheel[i], wheel[i+1])
        if temp == False:
            break
        if temp_d2 == - 1:
            temp_d2 = 1
        else:
            temp_d2 = -1
        change_list.append((i+1, temp_d2))
    for idx, d in change_list:
        wheel[idx] = rotate(wheel[idx], d)
    # print(change_list)
    # print(*wheel, sep='\n')
score = 0
for i in range(4):
    if wheel[i][0] == 1:
        score += (2 ** i)
print(score)
