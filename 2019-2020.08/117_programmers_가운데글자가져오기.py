def solution(s):
    idx = len(s) // 2
    length = len(s) % 2
    # 짝수일 경우
    if length == 0:
        return s[idx-1:idx+1]
    # 홀수일 경우
    else:
        return s[idx]

print(solution('abcd'))