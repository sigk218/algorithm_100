import sys
sys.stdin = open('input.txt', 'r')

# 번호를 붙여야함 ! -> 점수가 유일한 숫자가 아니다..

# 총 32개, scores[i] : i 번째 인덱스에 해당하는 점수
scores = [2*i for i in range(21)] + [13, 16, 19, 25, 30, 35, 22, 24, 28, 27, 26, 0]


route = [
    [i for i in range(21)] + [32],
    # 5로 분기
    [i for i in range(6)] + [i for i in range(21, 27)] + [20, 32],
    # 10으로 분기
    [i for i in range(11)] + [27, 28, 24, 25, 26, 20, 32],
    # 15로 분기
    [i for i in range(16)] + [29, 30, 31, 24, 25, 26, 20, 32]
]

# 중복 순열 세우기
def pick(d, x, score):
    global answer, t

    if d == 10:
        answer = max(answer, score)
    else:
        # 뽑을 수 있는 말이면 뽑는다
        for i in range(4):
            # 끝까지 도달한 말
            if visited[i] == 32:continue

            next_location = location[i] + arr[d]

            # 값 저장
            temp_w = way[i]
            temp_vi = visited[i]

            # 끝까지 갔다면(마지막 인덱스에 도착하면), 뽑고 넘어간다
            if next_location >= len(route[way[i]]):
                visited[i] = 32
                pick(d + 1, i, score)
                # 값 복원
                way[i] = temp_w
                visited[i] = temp_vi
                continue

            if way[i] == 0 and next_location < 20 and next_location % 5 == 0:
                way[i] = (next_location // 5)

            # 그 자리에 값이 있다면, 뽑지말고 넘어간다
            if route[way[i]][next_location] in visited:
                way[i] = temp_w
                continue

            location[i] += arr[d]
            visited[i] = route[way[i]][location[i]]
            pick(d + 1, i, score+scores[route[way[i]][location[i]]])

            # 값 복원
            visited[i] = temp_vi
            location[i] -= arr[d]
            way[i] = temp_w



# 말의 (상대) 위치 idx
location = [0, 0, 0, 0]
# 말의 (절대) 위치
visited = [0, 0, 0, 0]
# 말의 경로
way = [0, 0, 0, 0]
arr = list(map(int, input().split()))
answer = 0
pick(0, 0, 0)
print(answer)

# location에 절대적인 값이 들어가야함
# continue 이전에 복원... ㅜㅜ (58)
# ... 다시 풀어보기