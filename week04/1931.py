import sys

input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
    a, b = map(int, input().split())
    arr.append((a, b))

arr.sort(key=lambda x: (x[1], x[0]))

cnt = 0
time = 0
idx = 0

while idx < len(arr):
    if time <= arr[idx][0]:
        time = arr[idx][1]
        cnt += 1

    idx += 1

print(cnt)
