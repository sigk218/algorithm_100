def solution(arr):
    answer = [arr.pop(0)]
    for num in arr:
        if answer[-1] == num:
            continue
        else:
            answer.append(num)
    return answer

print(solution([1,1,3,3,0,1,1,]))