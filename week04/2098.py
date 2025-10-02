import sys

input = sys.stdin.readline

N = int(input())
costs = []

for _ in range(N):
    costs.append(list(map(int, input().split())))

dp = [[float("inf") for _ in range(N)] for _ in range((1 << N) + 1)]
dp[1 << 0][0] = 0

for visited in range(1 << N):
    for current_city in range(N):
        if not (visited & (1 << current_city)):
            continue

        for next_city in range(N):
            if visited & (1 << next_city):
                continue

            next_visited = visited | (1 << next_city)
            if costs[current_city][next_city]:
                dp[next_visited][next_city] = min(
                    dp[next_visited][next_city],
                    dp[visited][current_city] + costs[current_city][next_city],
                )

FULL = (1 << N) - 1
res = float("inf")

for i in range(N):
    if not costs[i][0]:
        continue
    cost = dp[FULL][i]
    res = min(res, cost + costs[i][0])
print(res)
