import sys

input = sys.stdin.readline

N = int(input())
edges = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

visited = [False for _ in range(N + 1)]


def dfs(V):
    stack = []
    stack.append(V)
    visited[V] = V
    while stack:
        pop = stack.pop()
        for vertex in edges[pop]:
            if not visited[vertex]:
                stack.append(vertex)
                visited[vertex] = pop


dfs(1)
for i in range(2, N + 1):
    print(visited[i])
