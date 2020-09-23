# 리턴하려는 배열이 빈 배열일 경우 -1
# 정렬을 하면 안댐 ㅜㅜ
def solution(arr):
    arr.remove(min(arr))
    return arr if arr else [-1]

print(solution([10]))