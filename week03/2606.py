import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
edges = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)


def visit(i, visited):
    stack = [i]
    visited[i] = True
    while stack:
        pop = stack.pop()
        for vertex in edges[pop]:
            if not visited[vertex]:
                stack.append(vertex)
                visited[vertex] = True


visit(1, visited)

print(sum(1 if x else 0 for x in visited) - 1)
