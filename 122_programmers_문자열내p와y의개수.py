# p와 y 모두 하나도 없는 경우는 항상 ture를 리턴
# 문제 잘 읽기 ! -> 대문자와 소문자는 구별하지 않음
def solution(s):
    pcnt, ycnt = 0, 0

    for si in s:
        if si == 'p' or si == 'P':
            pcnt += 1
        elif si == 'y' or si == 'Y':
            ycnt += 1

    if pcnt == 0 and ycnt == 0: return True
    if pcnt == ycnt: return True
    return False

# return s.lower().count('p') == s.lower().count('y')
# 대문자로 변환은 upper
# collections의 Counter이용하기

print(solution('pPoooyY'))

print('sss'.)