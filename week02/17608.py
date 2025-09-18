import sys

input = sys.stdin.readline

stack = []
size = 0

n = int(input())

for _ in range(n):
    number = int(input())
    while stack and stack[-1] <= number:
        size -= 1
        stack.pop()
    stack.append(number)
    size += 1

print(size)
