import sys

input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
    a, b = map(int, input().split())
    arr.append((a, b))

dp = [[0 for _ in range(N)] for _ in range(N)]

for length in range(1, N):
    for i in range(N - length):
        j = i + length
        dp[i][j] = float("inf")
        for k in range(i, j):
            dp[i][j] = min(
                dp[i][j],
                dp[i][k] + dp[k + 1][j] + arr[i][0] * arr[k][1] * arr[j][1],
            )
print(dp)
print(dp[0][N - 1])
