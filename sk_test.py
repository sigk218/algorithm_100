def solution(S, C):
    total_costs = 0
    flag = S[0]
    next_idx = 0
    start_idx = 0
    while True:
        next_idx += 1
        if next_idx >= len(S): break
        if flag != S[next_idx-1]:
            total_costs += sum(C[start_idx:next_idx]) - max(C[start_idx:next_idx])
            flag = S[next_idx-1]
            start_idx = next_idx
    return total_costs


print(solution('aabbbcc', [1, 2, 1, 2, 3, 1, 2]))