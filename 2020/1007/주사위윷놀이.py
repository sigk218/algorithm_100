import sys
sys.stdin = open('input.txt', 'r')

# 해당 말의 경로 결정 !
score = [
    [0, 2, 4, 6, 8, 10, 13, 16, 19, 25, 30, 35, 40],
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 25, 30, 35, 40],
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 28, 27, 26, 25, 30, 35, 40],
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],
]
# 어떤 말이 언제 갈 것인지 정하기 4 ** 10
arr = list(map(int, input().split()))
import itertools

answer = -1

for candidate in itertools.product([0, 1, 2, 3], repeat=10):

    # 현재 네개는 전부 출발 점 !
    location = [0, 0, 0, 0]
    # 경로도 모두 3 번째
    way = [3, 3, 3, 3]
    temp = 0
    my_score = [0, 0, 0, 0]
    for i in range(10):
        # print(way, my_score)
        # candidate[i] 번 말이 arr[i]칸 가기
        num = candidate[i]
        # 도착한 말이 골라지면 다음 경우로
        if location[num] == -1:
            break

        # 경로 바꿔주기
        if way[num] == 3:
            if location[num] + arr[i] == 5:
                way[num] = 0
            elif location[num] + arr[i] == 10:
                way[num] = 1
            elif location[num] + arr[i] == 15:
                way[num] = 2

        # 칸을 넘어가면 끝난다
        if location[num] + arr[i] >= len(score[way[num]]):
            location[num] = -1
            continue


        # 위치, 점수 업데이트
        location[num] += arr[i]
        this_score = score[way[num]][location[num]]
        if this_score in my_score:
            break
        my_score[num] = this_score
        temp += this_score
    # print(temp)
    answer = max(temp, answer)
    # break
print(answer)

# 방향이 3일때만 방향 전환을 할 수 있음
# 위치가 나의 위치랑 상대방의 위치랑 다를 수 있다 !
# 중복 값 -> visited 처리를 !!