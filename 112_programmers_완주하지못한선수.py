def solution(participant, completion):

    # participant = set(participant)
    # completion = set(completion)
    #
    # for answer in participant-completion:
    #     return answer


    num_people = len(completion)

    for i in range(num_people):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[i+1]

participant = ['leo', 'kiki', 'eden']
completion = ['eden', 'kiki']
print(solution(participant, completion))

# collection.Counter는 뺄셈이.. 가능 !
# 교집합으로는 풀 수 없다 -> 동명 이인 때문에 !