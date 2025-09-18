stack = []

n, k = map(int, input().split())

number = input()
popcount = 0

for digit in number:
    while stack and stack[-1] < digit and popcount < k:
        stack.pop()
        popcount += 1
    stack.append(digit)

while popcount < k:
    stack.pop()
    popcount += 1

print("".join(stack))
