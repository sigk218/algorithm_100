# 나누어 떨어지는 값을 오름차순으로 정렬
def solution(arr, divisor):
    answer = []
    while arr:
        num = arr.pop(0)
        if num % divisor == 0:
            answer.append(num)
    return sorted(answer) if answer else [-1]

print(solution([2, 36, 1, 3], 1))