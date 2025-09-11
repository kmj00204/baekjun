n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]
INF = float("inf")
dp = [[INF for _ in range(1 << n)] for _ in range(n)]

dp[0][1 << 0] = 0

for visited in range(1 << n):
    for current_city in range(n):
        if not visited & (1 << current_city):
            continue
        for next_city in range(n):
            if visited & (1 << next_city):
                continue
            if w[current_city][next_city] == 0:
                continue
            next_visited = visited | (1 << next_city)
            dp[next_city][next_visited] = min(
                dp[next_city][next_visited],
                dp[current_city][visited] + w[current_city][next_city],
            )

FULL = (1 << n) - 1
min_cost = INF

for last in range(n):
    if w[last][0] == 0:
        continue
    min_cost = min(min_cost, dp[last][FULL] + w[last][0])
print(min_cost)
