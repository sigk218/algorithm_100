import sys
sys.stdin = open('input.txt', 'r')

def choice(index, first, second):
    global answer
    if index == n:
        total1, total2 = 0, 0
        for f1 in first:
            for f2 in first:
                if f1 == f2: continue
                total1 += arr[f1-1][f2-1]
        for s1 in second:
            for s2 in second:
                if s1 == s2: continue
                total2 += arr[s1-1][s2-1]
        answer = min(answer, abs(total1-total2))
        return
    else:
        first.append(index+1)
        choice(index+1, first, second)
        first.pop()
        second.append(index+1)
        choice(index+1, first, second)
        second.pop()

# 각각의 사람이 어떤 팀에 들어갈 지
# 모든 사람을 결정 했으면 팀의 능력치차이를 최소
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
team = [0 for i in range(n)]
answer = 10000
choice(0, [], [])
print(answer)