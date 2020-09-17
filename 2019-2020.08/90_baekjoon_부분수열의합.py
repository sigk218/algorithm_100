import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
s = list(map(int, input().split()))
check = [0 for _ in range(20*100000+10)]


def solve(d, total):
    if d == n:
        check[total] = True
        return
    solve(d+1, total+s[d])
    solve(d+1, total)


solve(0, 0)
for i in range(20*100000+11):
    if check[i] == 0:
        break
print(i)