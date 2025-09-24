import sys

input = sys.stdin.readline

N, M = map(int, input().split())
half = N // 2

child = [[] for _ in range(N + 1)]
parent = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    child[a].append(b)
    parent[b].append(a)

result = 0


def visit_big(result, n):
    if len(parent[n]) == 0:
        return result
    for vertex in parent[n]:
        result.add(vertex)
        print(result)
        return visit_big(result, vertex)


big = set()
i = 1
b = visit_big(big, i)
print(b)
