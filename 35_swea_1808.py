import sys, itertools
sys.stdin = open('input.txt', 'r')

def s(n, cnt):
    global ans
    if n == 0: return
    c = chk(n)
    if c[0]:
        res = c[1] + cnt + 1
        if ans == - 1 or ans > res:
            ans = res
        return
    for x, y in a:
        if x != (0 or 1) and n % x == 0:
            s(n // x, cnt + y + 1)
    return
def chk(n):
    l = 0
    while n > 0:
        if d[n % 10] != 1:
            return (0, 0)
        l += 1
        n //= 10
    return (1, l)

T = int(input())
for t in range(1):
    d = list(map(int, input().split()))
    N = int(input())
    a = set()
    ans = - 1
    for i in range(2, int(N ** 0.5) + 1):
        if N % i == 0 and chk(i)[0]:
            a.add((i, chk(i)[1]))
    print(a)
    s(N, 0)
    print("#{} {}".format(t + 1, ans))

