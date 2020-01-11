import sys
sys.stdin = open('input.txt','r')

number = int(input())

def solve(n, iter):
    global answer
    if iter > answer:
        return
    if n == 1:
        # print(n, iter)
        answer = min(iter, answer)
        return 
    else:    
        solve(n - 1, iter+1)
        if n % 3 == 0:
            solve(n // 3, iter+1)
        if n % 2 == 0:
            solve(n // 2, iter+1)

answer = 10 ** 6 + 1
solve(number, 0)
print(answer)