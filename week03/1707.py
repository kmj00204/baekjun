import sys

sys.setrecursionlimit(100000)
from collections import deque

input = sys.stdin.readline

T = int(input())


def dfs(V, visited, edges):
    if visited[V]:
        return
    stack = deque()
    stack.append(V)
    visited[V] = 1
    while stack:
        pop = stack.pop()
        for vertex in edges[pop]:
            if not visited[vertex]:
                stack.append(vertex)
                visited[vertex] = -visited[pop]
            elif visited[vertex] == visited[pop]:
                return 0
    return 1


def myfun():
    V, E = map(int, input().split())
    edges = [[] for _ in range(V + 1)]

    for _ in range(E):
        a, b = map(int, input().split())
        edges[a].append(b)
        edges[b].append(a)

    visited = [0 for _ in range(V + 1)]

    result = 1
    for i in range(1, V + 1):
        if visited[i] == 0:
            result *= dfs(i, visited, edges)
    if result:
        print("YES")
    else:
        print("NO")


for _ in range(T):
    myfun()
