
def solution(answers):
    # 시험은 최대 10,000
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]
    answer = [0 for _ in range(3)]
    num_answers = len(answers)
    for i in range(num_answers):
        if answers[i] == s1[i%5]:
            answer[0] += 1
        if answers[i] == s2[i%8]:
            answer[1] += 1
        if answers[i] == s3[i%10]:
            answer[2] += 1

    return [i+1 for i, v in enumerate(answer) if v == max(answer)]

answers = [1,3,2,4,2]
print(solution(answers))

# 길이로 나는 것의 나머지 (모듈러 연산)
# enumerate의 사용
