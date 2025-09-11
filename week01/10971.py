n = int(input())
w = []
min_cost = float("inf")
visited = [False for _ in range(n)]

for _ in range(n):
    w.append(list(map(int, input().split())))


def func(depth, current_city, cost):
    global min_cost
    if depth == n and w[current_city][0] > 0:
        min_cost = min(min_cost, cost + w[current_city][0])
        return

    for next_city in range(n):
        if not visited[next_city] and w[current_city][next_city] > 0:
            visited[next_city] = True
            func(depth + 1, next_city, cost + w[current_city][next_city])
            visited[next_city] = False


visited[0] = True
func(1, 0, 0)
print(min_cost)
