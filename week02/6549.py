while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    arr = arr[1:]
    max_size = 0

    length = len(arr)
    stack = []

    for i in range(length):
        while stack and arr[stack[-1]] > arr[i]:
            pop_index = stack.pop()
            height = arr[pop_index]
            width = i if not stack else arr[stack[-1]]
            max_size = max(max_size, height * width)
        if not stack or (stack and arr[stack[-1]] != arr[i]):
            stack.append(i)

    while stack:
        pop_index = stack.pop()
        height = arr[pop_index]
        width = length if not stack else arr[stack[-1]]

        max_size = max(max_size, height * width)

    print(max_size)
