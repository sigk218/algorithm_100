import sys
sys.stdin = open('input.txt', 'r')

def check(shark):

    for s in shark[1:]:
        if s:
            return False
    return True

n, m, k = map(int, input().split())

# mymap -> 몇 번상어로 부터 왔는지, k, 비어있는지 차있는 건지
mymap = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]
# 좌표랑 방향
shark = [[0, 0, 0] for _ in range(m)]

# 초기 설정
for i in range(n):
    t = list(map(int, input().split()))
    for j in range(n):
        if t[j]:
            # 상어의 번호, k
            mymap[i][j] = [t[j]-1, k, 1]
            shark[t[j]-1][0] = i
            shark[t[j]-1][1] = j

    # 방향 설정
idx = 0
for d in list(map(int, input().split())):
    shark[idx][2] = d - 1
    idx += 1

pri = [[] for _ in range(m)]
for i in range(m):
    for j in range(4):
        t = []
        for nd in list(map(int, input().split())):
            t.append(nd-1)
        pri[i].append(t)

# print(*pri, sep='\n')
answer = -1
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for af in range(1000):

    # 좌표 : 번호, 방향
    new_smell = dict()
    for i in range(m):
        # 죽은 상어는 볼 필요 없다 !
        if not shark[i]:
            continue
        x, y, d = shark[i]
        candidate = []
        # 나의 방향과, 우선 순위에 따라 이동 방향을 결정한다
        for nd in pri[i][d]:
            xx = x + direction[nd][0]
            yy = y + direction[nd][1]
            if any([xx < 0, xx >= n, yy < 0, yy >= n]):
                continue
            if mymap[xx][yy][2]:
                if mymap[xx][yy][0] == i:
                    candidate.append((xx, yy, nd, i))
                continue
            if new_smell.get((xx, yy)) == None:
                new_smell[(xx, yy)] = [i, nd]
                break
            else:
                # 이동 후 한 칸에 여러마리 라면 -> 가장 작은 것이 생존한다
                if new_smell[(xx, yy)][0] > i:
                    new_smell[(xx, yy)][0] = [i, nd]
                break
        # 네 칸다 차있거나, 범위 밖으로 나간다면
        else:
            # 나의 냄새가 있는 곳에 냄새를 뿌린다
            (cx, cy, cd, num) = candidate[0]
            new_smell[(cx, cy)] = [num, cd]

    # map의 k를 감소시킨다
    for i in range(n):
        for j in range(n):
            if mymap[i][j][2] == 0:
                continue
            mymap[i][j][1] -= 1
            # k만큼 감소했을 경우, 칸을 비워준다
            if mymap[i][j][1] == 0:
                mymap[i][j] = [0, 0, 0]

    # 상어 정보를 업데이트 시킨다
    new_shark = [[] for _ in range(m)]
    # 해당 위치에 냄새를 뿌린다
    for key, value in new_smell.items():
        mymap[key[0]][key[1]] = [value[0], k, 1]
        new_shark[value[0]] = [key[0], key[1], value[1]]

    shark = new_shark

    if check(shark):
        answer = af+1
        break

    # print(af+1, '초 후')
    # print(*mymap, sep='\n')
    #
    # print(shark)
print(answer)
# 상어 움직임(상,하,좌,우 살피기 위해서) -> k값 감소, 새로운 값 내주기