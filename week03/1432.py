import heapq
import sys

input = sys.stdin.readline

n = int(input())
edges = [[] for _ in range(n + 1)]
indegree = [0 for _ in range(n + 1)]
answer = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    temp = list(map(int, input().strip()))
    for j in range(len(temp)):
        if temp[j] == 1:
            edges[j + 1].append(i)
            indegree[i] += 1


def sort():
    que = []
    for i in range(1, n + 1):
        if indegree[i] == 0:
            heapq.heappush(que, -i)

    cur_num = n
    while que:
        pop = -heapq.heappop(que)
        answer[pop] = cur_num
        cur_num -= 1
        for vertex in edges[pop]:
            indegree[vertex] -= 1
            if indegree[vertex] == 0:
                heapq.heappush(que, -vertex)

    if cur_num != 0:
        print(-1)
    else:
        print(" ".join(map(str, answer[1:])))


sort()
