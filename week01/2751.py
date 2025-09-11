import sys

n = int(sys.stdin.readline().strip("\n"))

arr = []

for _ in range(n):
    arr.append(int(sys.stdin.readline().strip("\n")))

arr.sort(reverse=False)

for a in arr:
    print(a)
