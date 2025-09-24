from collections import deque
import sys

input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

visited1 = [False for _ in range(N + 1)]
visited2 = [False for _ in range(N + 1)]


def dfs(V):
    stack = deque([V])
    while stack:
        pop = stack.pop()
        if visited1[pop]:
            continue
        visited1[pop] = True
        print(pop, end=" ")
        for i in range(N, 0, -1):
            if not visited1[i] and graph[pop][i]:
                stack.append(i)


def bfs(V):
    que = deque([V])
    visited2[V] = True
    while que:
        pop = que.popleft()
        print(pop, end=" ")
        for i in range(1, N + 1):
            if not visited2[i] and graph[pop][i]:
                que.append(i)
                visited2[i] = True


dfs(V)
print()
bfs(V)
