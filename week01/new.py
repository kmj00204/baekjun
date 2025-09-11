n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]

dp = [[float("inf") for _ in range(n)] for _ in range(1 << n)]
min_cost = float("inf")

dp[1 << 0][0] = 0

for visited in range(1 << n):
    for current_city in range(n):
        if not visited & (1 << current_city):
            continue
        for next_city in range(n):
            if visited & (1 << next_city):
                continue

            if w[current_city][next_city] == 0:
                continue

            new_visited = visited | (1 << next_city)
            dp[new_visited][next_city] = min(
                dp[new_visited][next_city],
                dp[visited][current_city] + w[current_city][next_city],
            )


for last in range(n):
    if w[last][0] == 0:
        continue
    min_cost = min(min_cost, dp[(1 << n) - 1][last] + w[last][0])

print(min_cost)
