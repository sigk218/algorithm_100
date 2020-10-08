def solution(numbers, hand):
    answer = ''
    # 오른 손, 왼 손 현재 위치
    right, left = 10, 11
    keypad = [(3, 1),
              (0, 0), (0, 1), (0, 2),
              (1, 0), (1, 1), (1, 2),
              (2, 0), (2, 1), (2, 2),
              (3, 2), (3, 0)]
    for num in numbers:
        # if number in [1, 4, 7]
        if any([num == 1, num == 4, num == 7]):
            left = num
            answer += 'L'
        elif num == 3 or num == 6 or num == 9:
            right = num
            answer += 'R'
        else:
            # 더 가까운 손가락
            dis_r = abs(keypad[right][0] - keypad[num][0]) + abs(keypad[right][1] - keypad[num][1])
            dis_l = abs(keypad[left][0] - keypad[num][0]) + abs(keypad[left][1] - keypad[num][1])
            if dis_r < dis_l:
                right = num
                answer += 'R'
            elif dis_r > dis_l:
                left = num
                answer += 'L'
            else:
                if hand == 'right':
                    right = num
                    answer += 'R'
                else:
                    left = num
                    answer += 'L'

    return answer

print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left'))