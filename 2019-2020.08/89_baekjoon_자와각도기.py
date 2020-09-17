import sys
sys.stdin = open('input.txt', 'r')

# 작도 할 때는 새로운 각을 이용해서 또다른 새로운 각을 만드는 것도 가능하다
# 현우가 외치는 각도를 창영이가 만들 수 있는지

n, k = map(int, input().split())
a = list(map(int, input().split()))
make = list(map(int, input().split()))
# 전체 각도가 360 밖에 안되기 때문에, 배열을 만들어서 저장 
#  d[i] = i인 각을 작도할 수 있는지 없는지
d = [0 for _ in range(360)]
# 0도는 가능하다
d[0] = 1
for i in range(n):
    # k를 하는 이유 : 각도가 1도면, 1을 360번 더하면 자기 자신
    for k in range(360):
        for j in range(360):
            if d[j] == 0:continue
            d[(j-a[i]+360) % 360] = 1
            d[(j+a[i]) % 360] = 1

for m in make:
    if d[m] == 0:
        print('NO')
    else:
        print('YES')