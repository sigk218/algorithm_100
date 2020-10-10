# 이런 식으로 구하는 것을 [유클리드 호제법]이라고 한다
# 두 자연수 A, B에 대하여 (A > B) A를 B로 나눈 나머지가 R
# 이때 A 와 B의 최대 공약수는 B와 R의 최대공약수와 같다
def solution(n, m):
    answer = []
    # 최대 공약수(GCD)
    x, y = n, m
    while y:
        x, y = y, x % y
    answer.append(x)

    # 최소 공배수
    answer.append((n*m)//x)
    return answer
print(solution(2, 5))


'''
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)
'''