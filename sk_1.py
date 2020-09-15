def solution(N):
    # write your code in Python 3.6
    if N % 2 == 0:
        answer = 'a' * (N - 1)
        return answer + 'b'
    return 'a' * N

print(solution(6))

