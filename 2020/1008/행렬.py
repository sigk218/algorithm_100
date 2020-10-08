import sys
sys.stdin = open('input.txt', 'r')

# https://www.acmicpc.net/problem/1080

# 만약 A를 B로 바꿀 수 없다면 -1을 출력한다 -> 이것을 고려안해서 한 번 틀렸다..;;
# 틀리면 최소 입력, 최대 입력 확인할 것
# 3 * 3 보다 작은 입력은 원소를 뒤집을 수는 없고, 확인만 한 후 답을 출력
# 3 * 3의 크기의 부분 행렬에 있는 모든 원소를 뒤집기

def part(x, y):

    for dx in range(3):
        for dy in range(3):
            if x + 3 > n or y + 3 > m:
                return 0
            A[x+dx][y+dy] = (A[x+dx][y+dy] + 1) % 2
    return 1

n, m = map(int, input().split())


A = [list(map(int, list(input()))) for _ in range(n)]
B = [list(map(int, list(input()))) for _ in range(n)]
# 3보다 크기가 작을 경우
if n < 3 or m < 3:
    if A == B:
        print(0)
        exit()
    else:
        print(-1)
        exit()

cnt = 0
for i in range(n):
    for j in range(m):
        if A[i][j] != B[i][j]:
            toggle = part(i, j)
            if toggle == 0: continue
            cnt += 1
            if A == B:
                print(cnt)
                exit()
print(-1)



