import sys

input = sys.stdin.readline

N, K = map(int, input().split())
arr = []

for _ in range(N):
    w, v = map(int, input().split())
    arr.append((w, v))

dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

# dp[i][j] == [i-1]번(idx) 까지의 아이템을 고려, [j] 만큼 담았을 때(현재 w의합),
# 보유한 'v'의 합

for i in range(N):
    for j in range(K + 1):
        weight = arr[i][0]
        value = arr[i][1]
        if weight + j > K:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j + weight] + value)

print(max(val for row in dp for val in row))
