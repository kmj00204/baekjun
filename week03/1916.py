import sys, heapq

input = sys.stdin.readline

N = int(input())
M = int(input())
cost = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    cost[a].append((b, c))


def dijkstra(start, end):
    heap = [(0, start)]
    total_cost = [float("inf") for _ in range(N + 1)]
    total_cost[start] = 0

    while heap:
        current_cost, current_city = heapq.heappop(heap)
        if current_cost > total_cost[current_city]:
            continue

        for next_city, next_cost in cost[current_city]:
            sum_cost = current_cost + next_cost
            if sum_cost < total_cost[next_city]:
                total_cost[next_city] = sum_cost
                heapq.heappush(heap, (sum_cost, next_city))
    return total_cost[end]


start, end = map(int, input().split())
print(dijkstra(start, end))
