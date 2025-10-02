import sys

input = lambda: sys.stdin.readline().rstrip()


def fun(n):
    arr = [0 for _ in range(n + 1)]
    arr[0] = 0
    arr[1] = 1
    for i in range(2, n + 1):
        arr[i] = arr[i - 2] + arr[i - 1]
    return arr[n]


n = int(input())
print(fun(n))
