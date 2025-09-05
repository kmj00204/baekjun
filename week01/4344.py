c = int(input())

for _ in range(c):
    arr = list(map(int, input().split()))
    total = 0
    for i in range(1, len(arr)):
        total += arr[i]
    avg = total / arr[0]
    hit = 0
    for i in range(1, len(arr)):
        if arr[i] > avg:
            hit += 1
    print(f"{(hit/arr[0]*100):.3f}%")
