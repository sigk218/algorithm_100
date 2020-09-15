def solution(S, C):


    end = False
    visited = [0 for _ in range(len(S))]
    visited[0] = 1
    now = S[0]
    answer = 0

    for i in range(1, len(S)):
        if visited[i]: continue
        t = [C[i-1]]
        if now == S[i]:
            t.append((C[i]))
            while True:
                i += 1
                if i >= len(S):
                    end = True
                    break
                if now == S[i]:
                    t.append(C[i])
                else:
                    break
            answer += sum(t) - max(t)
            # print(sum(t) - max(t))
        else:
            now = S[i]
        if end:
            break
    return answer

print(solution('abcccbd', [0, 1, 2, 3, 3, 4, 5]))