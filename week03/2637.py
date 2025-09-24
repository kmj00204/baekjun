from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
edges = [[] for _ in range(N + 1)]
indegree = [0 for _ in range(N + 1)]
result = [0 for _ in range(N + 1)]
result[N] = 1

for _ in range(M):
    a, b, c = map(int, input().split())
    edges[a].append((b, c))
    indegree[b] += 1


def fun():
    que = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            que.append(i)

    while que:
        pop = que.pop()
        for vertex, cnt in edges[pop]:
            result[vertex] += result[pop] * cnt
            indegree[vertex] -= 1
            if indegree[vertex] == 0:
                que.append(vertex)


fun()
for i in range(1, N + 1):
    if len(edges[i]) == 0:
        print(i, result[i])
