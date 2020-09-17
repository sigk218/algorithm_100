# 소수 찾기
# 짝수는 홀수가 될 수 없다
# 나 이상의 * 2를 지운다.
def solution(n):
    # 홀수만 가능함 -> 에라토스테네스의 체
    check = [i % 2 for i in range(n+1)]
    check[0] = 0
    for i in range(3, n+1, 2):
        # print(i, ' 번째')
        if check[i]:
            temp = i * 2
            while temp < n+1:
                check[temp] = 0
                temp += i
    return sum(check)

    # num=set(range(2,n+1))
    #
    # for i in range(2,n+1):
    #     if i in num:
    #         num-=set(range(2*i,n+1,i))
    # return len(num)

print(solution(10))