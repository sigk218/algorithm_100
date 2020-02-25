
# 순서별로 점수
scores = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40,
          13, 16, 19, 25, 26, 27, 28, 22, 24, 30, 35, 0]
# 경로
routes = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 32],
    # 5
    [0, 1, 2, 3, 4, 5, 21, 22, 23, 24, 30, 31, 20, 32],
    # 10
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 28, 29, 24, 30, 31, 20, 32],
    # 15
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 27, 26, 25, 24, 30, 31, 20, 32]
]
# 현재 말이 있는지 없는지

# 현재 말의 위치, 경로
horse = [[0, 0, 0] for _ in range(4)]

def pick(turn, score, num):
    global answer
    if turn == 10:
        answer = max(answer, score)
        # print('오예 ! 끝났다', score, horse)
    else:
        for i in range(4):
            # 가려고 하는 칸 구하기
            temp = horse[i][0] + commands[turn]
            # 매번 visited를 체크 해줘야 한다.

            visited = [0] * 33
            for loca, route_num, check in horse:
                if check == 1:continue
                visited[routes[route_num][loca]] = 1


            if temp < len(routes[horse[i][1]]) and visited[routes[horse[i][1]][temp]]:
                continue
            # 도착칸을 넘어가거나, 도착하면 이동을 마침
            if temp >= len(routes[horse[i][1]]):
                horse[i][2] = 1
                pick(turn+1, score, i)
                horse[i][2] = 0
                continue

            # 맵을 확인해준 수 경로 바꿔주기
            b_route = horse[i][1]
            if horse[i][1] == 0 and routes[horse[i][1]][temp] % 5 == 0 and routes[horse[i][1]][temp] <= 15:
                horse[i][1] = routes[horse[i][1]][temp] // 5
            horse[i][0] += commands[turn]
            pick(turn+1, score+scores[routes[horse[i][1]][horse[i][0]]], i)
            horse[i][0] -= commands[turn]
            horse[i][1] = b_route

import sys
sys.stdin = open('input.txt', 'r')
commands = list(map(int, input().split()))
answer = 0
pick(0, 0, 0)
print(answer)