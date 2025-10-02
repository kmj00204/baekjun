import sys

input = lambda: sys.stdin.readline().rstrip()


def fun(n):
    if n == 1 or n == 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b % 15746, (a + b) % 15746
    return b


n = int(input())
print(fun(n) % 15746)
