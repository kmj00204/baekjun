import sys

input = sys.stdin.readline

N, M = map(int, input().split())
edges = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)


def visit(n, visited):
    stack = [n]
    visited[n] = True
    while stack:
        pop = stack.pop()
        for vertex in edges[pop]:
            if not visited[vertex]:
                stack.append(vertex)
                visited[vertex] = True


count = 0
visited = [False for _ in range(N + 1)]
for i in range(1, N + 1):
    if not visited[i]:
        visit(i, visited)
        count += 1
    if all(x for x in visited[1:]):
        break
print(count)
