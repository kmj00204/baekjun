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


def visit_small(result, n):
    for vertex in child[n]:
        if vertex not in result:
            result.add(vertex)
            visit_small(result, vertex)
    return result


def visit_big(result, n):
    for vertex in parent[n]:
        if vertex not in result:
            result.add(vertex)
            visit_big(result, vertex)
    return result


result = []
for i in range(1, N + 1):
    small = set()
    big = set()
    s = visit_small(small, i)
    b = visit_big(big, i)
    if (s and len(s) > half) or (b and len(b) > half):
        result.append(i)

print(len(result))
