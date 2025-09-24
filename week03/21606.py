import sys

input = sys.stdin.readline

N = int(input())
inside = int(input()[::-1] + "0", 2)
edges = [[] for _ in range(N + 1)]
result = 0

for _ in range(N - 1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)
    if inside & (1 << a) and inside & (1 << b):
        result += 2


def dfs(V):
    stack = [V]
    visited = 1 << V
    global result, linked
    cnt = 0
    while stack:
        pop = stack.pop()
        for vertex in edges[pop]:
            if not visited & 1 << vertex:
                visited |= 1 << vertex
                if not inside & 1 << vertex:
                    stack.append(vertex)
                    linked |= 1 << vertex
                else:
                    cnt += 1
    if cnt < 2:
        return
    result += cnt * (cnt - 1)


linked = 0
for i in range(1, N + 1):
    if not inside & 1 << i:
        if linked & 1 << i:
            continue
        linked |= 1 << i
        dfs(i)
print(result)
