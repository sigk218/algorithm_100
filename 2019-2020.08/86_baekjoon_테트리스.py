import sys
sys.stdin = open('input.txt', 'r')

n, p = map(int, input().split())

arr = list(map(int, input().split()))

answer = 0
for i in range(n):
    if p == 1:
        answer += 1
        if i+3 < n and arr[i] == arr[i+1] and arr[i+1] == arr[i+2] and arr[i+2] == arr[i+3]:
            answer += 1
    elif p == 2:
        if i+1 < n and arr[i] == arr[i+1]:
            answer += 1
    elif p == 3:
        if i + 2 < n and arr[i] == arr[i+1] and arr[i+1] +1== arr[i+2]:
            answer += 1
        if i + 1 < n and arr[i] == arr[i+1] +1:
            answer += 1
    elif p == 4:
        if i + 2 < n and arr[i] == arr[i+1]+1 and arr[i+1] == arr[i+2]:
            answer += 1
        if i + 1 < n and arr[i]+1 == arr[i+1]:
            answer += 1
    elif p == 5:
        if i + 2 < n:
            if arr[i] == arr[i+1] and arr[i+1] == arr[i+2]:
                answer +=1
            if arr[i] == arr[i+1] + 1 and arr[i+1] + 1 == arr[i+2]:
                answer += 1
        if i+1 < n:
            if arr[i] +1 == arr[i+1]:
                answer += 1
            if arr[i] == arr[i+1] + 1:
                answer += 1
    elif p == 6:
        if i+2 <n:
            if arr[i] == arr[i+1] and arr[i+1] == arr[i+2]:
                answer +=1
            if arr[i] +1 == arr[i+1] and arr[i+1] == arr[i+2]:
                answer += 1
        if i+1 <n:
            if arr[i] == arr[i+1]:
                answer += 1
            if arr[i] == arr[i+1] + 2:
                answer += 1
    elif p == 7:
        if i+2 <n:
            if arr[i] == arr[i+1] and arr[i+1] == arr[i+2]:
                answer += 1
            if arr[i+2] + 1 == arr[i+1] and arr[i] == arr[i+1]:
                answer += 1
        if i+1 <n:
            if arr[i] + 2 == arr[i+1]:
                answer += 1
            if arr[i] == arr[i+1]:
                answer += 1



print(answer)