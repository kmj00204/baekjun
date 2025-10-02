import sys, math

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [True for _ in range(N + 1)]
for _ in range(M):
    arr[int(input())] = False

# x = int(math.ceil(-1 + (1 + 8 * N) ** 0.5) / 2)
x = int((2 * N) ** 0.5) + 2
dp = [[float("inf") for _ in range(x + 1)] for _ in range(N + 1)]

if arr[2]:
    dp[2][1] = 1
else:
    print(-1)
    exit()

for i in range(2, N + 1):
    for j in range(x):
        if dp[i][j] == float("inf"):
            continue
        for dj in [-1, 0, 1]:
            new_j = j + dj
            if new_j < 1:
                continue
            if 0 <= i + new_j < N + 1 and arr[i + new_j]:
                dp[i + new_j][new_j] = min(dp[i + new_j][new_j], dp[i][j] + 1)

res = min(dp[N])
if res == float("inf"):
    print(-1)
else:
    print(res)
