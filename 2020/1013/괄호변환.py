# 균형 잡힌 괄호 문자열의 인덱스 반환하기
def make_balance(p):
    # 왼쪽 괄호의 갯수
    cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        else:
            cnt -= 1

        if cnt == 0:
            return i

# 올바른 괄호 문자열인지 검사
def check(p):
    cnt = 0
    for c in p:
        if c == '(':
            cnt += 1
        else:
            if cnt == 0:
                return False
            cnt -= 1
    return True


def solution(p):

    if p == '':
        return p

    idx = make_balance(p)
    u = p[:idx+1]
    v = p[idx+1:]

    if check(u):
        return u + solution(v)

    answer = '('
    answer += solution(v)
    answer += ')'
    u = list(u[1:-1])
    for i in range(len(u)):
        if u[i] == '(':
            u[i] = ')'
        else:
            u[i] = '('
    return answer + ''.join(u)


print(solution("()))((()"))