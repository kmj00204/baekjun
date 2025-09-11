n = int(input())
arr = list(map(int, input().split()))
visited = [False] * n
stack = []
max_result = 0


def func(depth):
    global max_result
    if depth == n:
        temp_max = sum(abs(stack[i + 1] - stack[i]) for i in range(n - 1))
        max_result = max(max_result, temp_max)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            stack.append(arr[i])
            func(depth + 1)
            stack.pop()
            visited[i] = False


func(0)
print(max_result)
