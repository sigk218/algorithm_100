import sys
sys.stdin = open('input.txt', 'r')

# N 은 짝수이며, 두 팀으로 나눠야 한다
# 능력치
# 능력치의 차이를 최소로

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

member = {ni for ni in range(n)}
answer = 1000000
import itertools
for teamA in list(itertools.combinations(member, n//2)):
    scoreA, scoreB = 0, 0
    teamB = member-set(teamA)
    teamB = list(teamB)
    # print(teamA, teamB)


    for i in range(n//2-1):
        for j in range(i, n//2):
            scoreA += arr[teamA[i]][teamA[j]]
            scoreA += arr[teamA[j]][teamA[i]]
            scoreB += arr[teamB[i]][teamB[j]]
            scoreB += arr[teamB[j]][teamB[i]]
    answer = min(answer, abs(scoreA-scoreB))
    # print(teamA, teamB)
    # print(scoreA, scoreB)
print(answer)

