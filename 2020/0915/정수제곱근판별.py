def solution(n):
    flag = False
    x = n ** (1/2)
    if int(x) ** 2 == n:
        flag = True
        # print(n)
    return int((x+1) ** 2) if flag else -1

print(solution(3))