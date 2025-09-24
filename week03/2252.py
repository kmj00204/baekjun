import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
edges = [[] for _ in range(N + 1)]
indegree = [0 for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    indegree[b] += 1


def sorts(edges):
    que = deque()
    result = []
    for i in range(1, N + 1):
        if indegree[i] == 0:
            que.append(i)

    while que:
        pop = que.popleft()
        result.append(pop)
        for vertex in edges[pop]:
            indegree[vertex] -= 1
            if indegree[vertex] == 0:
                que.append(vertex)
    return result


print(" ".join(map(str, sorts(edges))))
