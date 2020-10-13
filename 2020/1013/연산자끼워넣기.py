import sys
sys.stdin = open('input.txt', 'r')

# 이때 주어진 수의 순서를 바꾸면 안된다
# 우선 순위를 무시하고 앞에서 부터 진행
# 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램
def cal(a, ex, b):
    if ex == 0:
        return a + b
    elif ex == 1:
        return a - b
    elif ex == 2:
        return a * b
    else:
        # 나눗셈은 양수로 바꾼뒤 몫을 취하고, 몫을 음수로 바꾼 것과 같다
        return int(a / b)

def choice(d, expression, result):
    global min_answer, max_answer

    if d == n-1:
        min_answer = min(min_answer, result)
        max_answer = max(max_answer, result)
        return

    for i in range(4):
        if expression[i]:
            expression[i] -= 1
            choice(d+1, expression, cal(result, i, arr[d+1]))
            expression[i] += 1


n = int(input())
arr = list(map(int, input().split()))
ex = list(map(int, input().split()))
min_answer, max_answer = 10000000001, -10000000001
choice(0, ex, arr[0])
print(max_answer)
print(min_answer)