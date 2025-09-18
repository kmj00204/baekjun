n = int(input())
arr = list(map(int, input().split()))

arr.sort()

left = 0
right = n - 1
min_sum = float("inf")
min_left = left
min_right = right

while left < right:
    sum_of_lr = arr[left] + arr[right]

    if min_sum > abs(sum_of_lr):
        min_sum = abs(sum_of_lr)
        min_left = left
        min_right = right

    if sum_of_lr == 0:
        print(arr[left], arr[right])
        break
    if sum_of_lr > 0:
        right = right - 1

    if sum_of_lr < 0:
        left = left + 1

print(arr[min_left], arr[min_right])
