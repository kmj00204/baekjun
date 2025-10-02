import sys

input = sys.stdin.readline


def fun():
    N = int(input())
    arr = []

    for _ in range(N):
        a, b = map(int, input().split())
        arr.append((a, b))

    arr.sort()
    cnt = 1
    score = arr[0][1]

    for i in range(1, N):
        if arr[i][1] < score:
            score = arr[i][1]
            cnt += 1

    print(cnt)


T = int(input())
for _ in range(T):
    fun()
