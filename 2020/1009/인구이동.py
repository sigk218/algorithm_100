import sys
sys.stdin = open('input.txt', 'r')

n, l, r = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

def end():
    idx = 0
    for i in range(n):
        for j in range(n):
            idx += 1
            if unit[i][j] != idx:
                return False
    return True

import collections
def find_unit(num, i, j):

    people = arr[i][j]
    unit[i][j] = num
    country = [(i, j)]
    #num 번째 연합을 찾아서 표시해주기
    q = collections.deque()
    q.append((i, j))
    while q:
        x, y = q.popleft()
        for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
            xx = x + dx
            yy = y + dy
            if xx < 0 or xx >= n or yy < 0 or yy >= n: continue
            if unit[xx][yy]: continue
            diff = abs(arr[x][y] - arr[xx][yy])
            if diff < l or diff > r: continue
            q.append((xx, yy))
            unit[xx][yy] = num
            people += arr[xx][yy]
            country.append((xx, yy))
    return people, country

# 인구 이동이 발생하는 횟수
for cnt in range(2001):
    unit = [[0 for _ in range(n)] for _ in range(n)]
    num = 0
    
    # 국경선을 열고, 연합을 만든다
    move = []
    for i in range(n):
        for j in range(n):
            if unit[i][j]: continue
            num += 1
            people, country = find_unit(num, i, j)
            if country:
                new_people = people // len(country)
                for (x, y) in country:
                    arr[x][y] = new_people
            # if country:
            #     move.append((people, country))

    if end():
        print(cnt)
        break

    # # 인구이동 시작
    # for (people, country) in move:
    #     new_people = people // len(country)
    #     for (x, y) in country:
    #         arr[x][y] = new_people
            

# 처음에 숫자 셀때, 나 체크해주는거랑 (bfs) 나를 country에 넣어주는 것을 까먹음
# 연합 숫자 올려주는거 까먹음
# 아.. 뭔가 분명히... 이전이랑 비슷하게 푸는데, 괜히 시간 재고 푸니까 떨림..
# 유닛 체크랑, 인원 채우는거 좀 더 빠르게 바꿀 수 있을듯 ? -> 고쳤더니 빨라짐 !