def solution(n, lost, reserve):

    # 여벌의 체육복이 있는 학생도 도난 당했을 수 있다.
    # 모든 학생이 1벌의 체육복을 가지고 있다.
    status = [1 for _ in range(n)]
    # 잃어버린 학생은 -1
    for stu in lost:
        status[stu-1] -= 1
    # 여벌이 있는 학생은 +1
    for stu in reserve:
        status[stu-1] += 1
    for i in range(n):
        if not status[i]:
            if i-1 >= 0 and status[i-1] > 1:
                status[i-1] -= 1
                status[i] += 1
            elif i+1 < n and status[i+1] > 1:
                status[i+1] -= 1
                status[i] += 1

    # 이렇게 쓰는 것도 가능함 : len([x for x in n if x != 0])
    return sum(map(bool, status))
print(solution(5, [2,4], [1, 3, 5]))