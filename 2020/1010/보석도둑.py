import sys
sys.stdin = open('input.txt', 'r')

# N개의 보석
# 무게와 가격
# 가방에는 최대 한개의 보선만 넣을 수 있다.
# 상덕이가 훔칠 수 있는 보석 가격의 합
# 문제 : https://www.acmicpc.net/problem/1202
# 풀이 참고 : https://it-garden.tistory.com/291

import heapq
n, k = map(int, input().split())
jewelry = []
for _ in range(n):
    m, v = map(int, input().split())
    heapq.heappush(jewelry, [m, v])

backpack = [int(input()) for _ in range(k)]
backpack.sort()

answer = 0
p = []
for i in range(k):
    # 현재 가방에 담을 수 있는 무게
    capa = backpack[i]

    # 가방에 담을 수 있는 a에 있는 모든 보석
    while jewelry and capa >= jewelry[0][0]:
        [m, v] = heapq.heappop(jewelry)
        # 값을 -로 넣어서 최대힙 만들기
        heapq.heappush(p, -v)

    if p:
        answer -= heapq.heappop(p)
    elif not jewelry:
        break
print(answer)
