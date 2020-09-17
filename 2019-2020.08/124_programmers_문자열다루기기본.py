# isalpha, isdigit
# 문제 꼼꼼히 읽기 -> 문자열의 길이가 4, 6이여야 한다!
# isdigit 을 한번에 비교해도 된다 !
def solution(s):
    if not len(s) in (4, 6): return False
    for si in s:
        if not si.isdigit():
            return False
    return True
# return s.isdigit() and len(s) in (4, 6)
print(solution('a234'))