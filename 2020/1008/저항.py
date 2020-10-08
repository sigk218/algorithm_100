import sys
sys.stdin = open('input.txt', 'r')

# https://www.acmicpc.net/problem/1076

resistance = ['black', 'brown', 'red', 'orange', 'yellow', 'green',
              'blue', 'violet', 'grey', 'white']

answer = 0
for i in range(2):
    t = resistance.index(input())
    answer += t * (10 ** (2-i-1))
print(answer * (10 ** resistance.index(input())))