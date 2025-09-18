import heapq

n = int(input())
arr = [int(input()) for _ in range(n)]
heapq.heapify(arr)

answer = 0

if len(arr) < 3:
    if len(arr) == 1:
        print(0)
        exit()
    print(sum(arr))
    exit()

while len(arr) > 2:
    first_min = heapq.heappop(arr)
    second_min = heapq.heappop(arr)

    answer += first_min + second_min

    heapq.heappush(arr, first_min + second_min)

answer += arr[0] + arr[1]

print(answer)
