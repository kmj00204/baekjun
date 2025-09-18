import sys

input = sys.stdin.readline

arr = []

n = int(input())
for _ in range(n):
    mid, rad = map(int, input().split())
    arr.append(("l", mid - rad))
    arr.append(("r", mid + rad))

arr.sort(key=lambda x: (x[1], -ord(x[0])))

stack = []
count = 1

for dir, num in arr:
    if dir == "l":
        stack.append((dir, num))
    else:
        total = 0
        while stack:
            prev = stack.pop()
            if prev[0] == "l":
                width = num - prev[1]

                if total == width:
                    count += 2
                else:
                    count += 1
                stack.append(("c", width))
                break
            if prev[0] == "c":
                total += prev[1]


print(count)
