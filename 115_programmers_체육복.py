def pick(d, cnt, num_lost, lost, n):
    global answer, check
    # print(d, cnt, num_lost)
    if d == num_lost:
        answer = max(answer, cnt)
        return
    else:
        for di in [1, -1]:
            idx = lost[d] - 1
            if idx+di < n and check[idx+di] and idx+di not in lost:
                check[idx+di] = 0
                pick(d+1, cnt+1, num_lost, lost, n)
                check[idx+di] = 1
            else:
                pick(d + 1, cnt, num_lost, lost, n)

def solution(n, lost, reserve):
    global check, answer

    # 체육 수업을 들을 수 있는 학생의 최대값
    num_lost = len(lost)
    check = [0 for _  in range(n)]
    for stu in reserve:
        check[stu-1] = 1
    answer = n - num_lost
    pick(0, n-num_lost, num_lost, lost, n)
    return answer

n = 3
lost = [3]
reserve = [1]
print(solution(5, [2,3], [3,4]))