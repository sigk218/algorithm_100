# 큰 것부터 차례대로 -> 내림차순
# 대문자가 더 큰 것으로 매겨져서 대, 소문자를 따로 할 필요가 x
def solution(s):
    low = ''
    up = ''
    for si in s:
        if si.islower():
            low += si
        else:
            up += si
    return ''.join(sorted(list(low), reverse=True))+''.join(sorted(list(up), reverse=True))
print(solution('Zbcdefg'))