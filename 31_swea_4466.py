import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
for tc in range(T):
    n, k = map(int, input().split())
    scores = list(map(int, input().split()))
    scores.sort(reverse=True)
    print('#{} {}'.format(tc+1, sum(scores[0:k])))