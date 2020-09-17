import sys, math
sys.stdin = open('input.txt', 'r')

# 처음에는 한 경우당 감독의 수가 1번인줄 알 고 어렵게 생각해버림...
n = int(input())
students = list(map(int, input().split()))
b, c = map(int, input().split())


# for s in students:
#     people += 1
#     if s - b <= 0:
#         pass
#     else:
#         people += math.ceil((s - b) / c)
# print(people)

people = 0
for s in students:
    people += 1
    temp = s - b
    # 사람 수니까 양수
    if s - b > 0:
        if temp % c:
            people += temp // c + 1
        else:
            people += temp // c
print(people)

