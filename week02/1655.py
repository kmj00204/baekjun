import heapq, sys

input = sys.stdin.readline

small = []
big = []

n = int(input())

for _ in range(n):
    num = int(input())
    if len(small) == len(big):
        heapq.heappush(small, -num)
    else:
        heapq.heappush(big, num)

    if big and -small[0] > big[0]:
        small_num = -small[0]
        big_num = big[0]

        if small_num > big_num:
            small_pop = -heapq.heappop(small)
            big_pop = -heapq.heappop(big)
            heapq.heappush(small, big_pop)
            heapq.heappush(big, small_pop)

    print(-small[0])
