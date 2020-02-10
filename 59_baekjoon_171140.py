import sys
sys.stdin = open('input.txt', 'r')

# 1초가 지날 때마다 배열에 연산이 적용
#  런타임에러 -> r,c 조건 잘 볼 것 !
# 아래 와같은 경우가 나올 수 있음
'''
4 4 4
3 3 3
3 3 3
3 3 3
'''
# (횟수, 숫자) -> 횟수가 같다면 숫자는 작은 순서대로
cnt = 0
def mysort(li):
    new_li = [0] * 100
    cnt = [0] * 101
    for i in range(len(li)):
        cnt[li[i]] += 1
    sorted_cnt = []
    for i in range(1, 101):
        if cnt[i]:
            sorted_cnt.append((cnt[i], i))
    sorted_cnt.sort()
    i = 0
    for iter, number in sorted_cnt:
        if number == 0 or iter == 0: continue
        new_li[i] = number
        new_li[i+1] = iter
        i += 2
    return new_li, 2 * len(sorted_cnt)

# 행렬을 맞춰서 0이 채워진다
# 정렬할때 0은 무시한다
# 최대 100 X 100
# A[r][c] 이 k가 되기 위한 최소시간


r, c, k = map(int, input().split())
r -= 1
c -= 1
li = [list(map(int, input().split())) for _ in range(3)]
next_li = [[0] * 100 for _ in range(100)]
num_c, num_r = 3, 3
for i in range(3):
    for j in range(3):
        next_li[i][j] = li[i][j]


# next_li = [[2, 1, 1, 2, 0, 0],
# [1, 1, 2, 1, 3, 1],
# [3, 3, 0, 0, 0, 0]]
# num_c, num_r = 3, 6
# 1. R연산 : 행의개수>= 열의 개수 -> 배열 a의 모든 행 정렬
# 2. C연산 : 행의 개수<열의개수 -> 배열 a의 모든 열 정렬
# print(next_li[r][c])
while next_li[r][c] != k:
    # print(next_li[r][c])
    if num_c >= num_r:
        temp_li = [[0] * 100 for _ in range(100)]
        tempr = num_r
        for i in range(num_c):
            small_li = []
            for j in range(tempr):
                small_li.append(next_li[i][j])
            temp, result_r = mysort(small_li)
            for j in range(result_r):
                temp_li[i][j] = temp[j]
            num_r = max(result_r, num_r)
        # print(*next_li, sep='\n')
        # print(num_r)
    else:
        temp_li = [[0] * 100 for _ in range(100)]
        tempc = num_c
        for j in range(num_r):
            small_li = []
            for i in range(tempc):
                small_li.append(next_li[i][j])
            # print(small_li)
            temp, result_c = mysort(small_li)
            # print(temp)
            # print(result_c)
            for i in range(result_c):
                if temp[i] == 0: break
                temp_li[i][j] = temp[i]
            num_c = max(result_c, num_c)
        # print(*temp_li, sep='\n')
    next_li = temp_li
    cnt += 1
    if cnt > 101:
        cnt = -1
        break
# print(next_li[r][c])
print(cnt)