import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
arr = list(map(int, input().split()))
b, c = map(int, input().split())

# 총 감독관은 무조건 들어간다
answer = n
for i in range(n):
    arr[i] -= b
    # 이 줄을 넣어줘야한다 ! !
    if arr[i] < 0: continue
    answer += arr[i] // c
    if arr[i] % c:
        answer += 1
print(answer)

