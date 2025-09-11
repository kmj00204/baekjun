import sys

n = int(sys.stdin.readline().strip("\n"))
idx = [0] * 10001

for _ in range(n):
    number = int(sys.stdin.readline().strip("\n"))
    idx[number] += 1

for i in range(10001):
    if idx[i] > 0:
        for _ in range(idx[i]):
            sys.stdout.write(f"{i}\n")
