# 굉장히 많이 나오는 정렬 문제 ..
# 파이썬의 스페셜 메서드(매직메서드) -> 더블언더스코어, 미리 정의 되어있는 Built-in 함수들이
# 처리할 연산을 재정의 하거나, 사용자가 원하는 대로 사용할 수 있다.
# 정렬을 한번 해주고, 다시 문자열을 기준으로 정렬 해줘야한다.
def solution(strings, n):
    strings.sort(key=lambda string: (string[n], string))
    return strings

print(solution(['sun', 'bed', 'car'], 1))