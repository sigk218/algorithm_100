# https://www.acmicpc.net/problem/1339
# n개의 단어로 이루어져있음

# 각 자리의 중요도를 기록한다 
# 알파벳의 개수는 26개

import sys
sys.stdin = open('input.txt', 'r')


a = int(input())
alpha = [0 for _ in range(26)]
for _ in range(a):
    s1 = input()

    for i in range(len(s1)):
        alpha[ord(s1[i]) - ord('A')] += 10 ** (len(s1)-1-i)


answer = 0
# 내림차순 정렬
alpha.sort(reverse=True)
idx = 0

for i in range(9, 0, -1):
    answer += alpha[idx] * i
    idx += 1
print(answer)