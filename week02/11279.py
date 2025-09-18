import heapq, sys

input = sys.stdin.readline
heap = []

heapq.heapify(heap)

n = int(input())
for _ in range(n):
    put = int(input())
    if not put:
        if len(heap) < 1:
            print(0)
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -put)
