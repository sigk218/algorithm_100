import sys
sys.stdin = open('input.txt', 'r')

target = input().replace(',','').replace(';','').split(' ')

for i in range(1, len(target)):
    answer = target[0]
    for j in range(len(target[i])-1, -1, -1):
        if target[i][j].isalpha():break
        if target[i][j] == '[':
            answer += ']'
        elif target[i][j] == ']':
            answer += '['
        else:
            answer += target[i][j]
    answer += ' '
    answer += target[i][:j+1]
    answer += ';'
    print(answer)

