def solution(a, b):
    # 목요일 철자 오타..........
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    end_of_month = [31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366]

    if a > 1:
        idx = end_of_month[a-2]
    else:
        idx = 0

    idx += b - 1
    idx %= 7
    return day[idx]

print(solution(1, 2))
