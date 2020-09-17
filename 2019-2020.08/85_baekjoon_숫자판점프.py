import sys
sys.stdin = open('input.txt', 'r')

# 임의의 위치에서 시작
# 0 ~ 9
# 네 방향으로 다섯 번 이동
# 거쳤던 칸을 다시 거쳐도 댐
# 서로 다른 여섯자리의 수들의 개수

arr = [list(map(int, input().split())) for _ in range(5)]
# print(*arr, sep='\n')

def solve(d, x, y, t):
    global answer
    # print(d, x, y, t)
    if d > 5: return
    if d == 5:
        answer.add(t)
        # print(t)
    else:
        for dx, dy in (0, 1), (1, 0), (-1, 0), (0, -1):
            if 0 <= x + dx < 5 and 0 <= y + dy < 5:
                solve(d+1, x+dx, y+dy, t+str(arr[x+dx][y+dy]))




answer = set()
visited = [[0 for _ in range(5)] for _ in range(5)]
for i in range(5):
    for j in range(5):
        solve(0, i, j, str(arr[i][j]))
# print(answer)
print(len(answer))