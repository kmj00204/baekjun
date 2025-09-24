import sys

input = sys.stdin.readline


def divide(a, b):
    if a > 0:
        result = a // b
    else:
        result = -(-a // b)
    return result


def operate(op, a, b):
    if op == 0:
        return a + b
    if op == 1:
        return a - b
    if op == 2:
        return a * b
    if op == 3:
        if a > 0:
            return a // b
        else:
            return -(abs(a) // b)


N = int(input())
numbers = list(map(int, input().split()))
operands = list(map(int, input().split()))

max_res = -float("inf")
min_res = float("inf")

result = numbers[0]
depth = 0


def backtrack(depth, result):
    global min_res, max_res
    if depth == N:
        min_res = min(min_res, result)
        max_res = max(max_res, result)

    for i in range(4):
        if operands[i] > 0:
            operands[i] -= 1
            backtrack(depth + 1, operate(i, result, numbers[depth]))
            operands[i] += 1


backtrack(1, result)
print(max_res)
print(min_res)
