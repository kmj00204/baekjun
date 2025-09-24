import sys, heapq

input = sys.stdin.readline

v, e = map(int, input().split())
graph = [[] for _ in range(v)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a - 1].append((c, b - 1))
    graph[b - 1].append((c, a - 1))

visited = [False for _ in range(v)]

heap = []
heapq.heappush(heap, (0, 0))
result = 0

while heap:
    cost, vertex = heapq.heappop(heap)
    if visited[vertex]:
        continue
    visited[vertex] = True
    result += cost

    for next_cost, next_vertex in graph[vertex]:
        if not visited[next_vertex]:
            heapq.heappush(heap, (next_cost, next_vertex))

print(result)
