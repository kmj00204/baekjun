from collections import deque
import sys

input = sys.stdin.readline

N, M, K, X = map(int, input().split())
edges = [[] for _ in range(N + 1)]
result = []

for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)


def bfs(start, visited, k):
    que = deque()
    que.append((start, k))
    visited[start] = True
    while que:
        pops = que.popleft()
        pop = pops[0]
        if pops[1] == 0:
            result.append(pop)
        for vertex in edges[pop]:
            if not visited[vertex]:
                que.append((vertex, pops[1] - 1))
                visited[vertex] = True


visited = [False for _ in range(N + 1)]
bfs(X, visited, K)
if len(result) == 0:
    print(-1)
else:
    result.sort()
    for item in result:
        print(item)
