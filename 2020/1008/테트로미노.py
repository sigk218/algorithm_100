import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def makemini(x, y):
    global answer

    for mini in shape:
        temp = 0
        flag = False
        for dx in range(len(mini)):
            for dy in range(len(mini[0])):
                if i + dx < 0 or i + dx >= n or j + dy < 0 or j + dy >= m:
                    flag = True
                    break
                temp += arr[i + dx][j + dy] * mini[dx][dy]
            if flag:
                break
        else:
            answer = max(answer, temp)


shape = [
    # ㅗ 모양
    [[1, 1, 1], [0, 1, 0]],
    [[0, 1, 0], [1, 1, 1]],
    [[0, 1], [1, 1], [0, 1]],
    [[1, 0], [1, 1], [1, 0]],

    # ㅣ
    [[1, 1, 1, 1]],
    [[1], [1], [1], [1]],

    # ㅁ
    [[1, 1], [1, 1]],

    # L
    [[1, 0], [1, 0], [1, 1]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1], [0, 1], [0, 1]],
    [[0, 0, 1], [1, 1, 1]],
    [[1, 1], [1, 0], [1, 0]],
    [[1, 0, 0], [1, 1, 1]],
    [[0, 1], [0, 1], [1, 1]],
    [[1, 1, 1], [0, 0, 1]],

    # 이상한 거..
    [[1, 0], [1, 1], [0, 1]],
    [[0, 1], [1, 1], [1, 0]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 1, 0], [0, 1, 1]]
]



answer = -1
for i in range(n):
    for j in range(m):
        makemini(i, j)
print(answer)


# 괜히... dfs로 시도했다가.. ㅜㅜ
# 풀던대로 풀자.. ! ㅜㅜ 원래방법대로 풀었으면 훠어어얼씬 빨리 풀었을듯
# 10 : 38