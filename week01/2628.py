w, h = map(int, input().split())
num_of_lines = int(input())

arr = [["O" for _ in range(w)] for _ in range(h)]
sawa = []
sawb = []


def smallthan(saw, b):
    result = 0
    for a in saw:
        if a < b:
            result += 1
    return result


for _ in range(num_of_lines):
    a, b = map(int, input().split())
    if a == 0:
        arr.insert(b + smallthan(sawa, b), ["X" for _ in range(len(arr[0]))])
        sawa.append(b)

    if a == 1:
        sawb.sort()
        for i in range(len(arr)):
            arr[i].insert(b + smallthan(sawb, b), "X")
        sawb.append(b)

# for i in range(len(arr)):
#     print(arr[i])


def best_land(arr):
    rows = len(arr)
    cols = len(arr[0])

    visited = [[False for _ in range(cols)] for _ in range(rows)]

    def dfs(r, c):

        if r < 0 or r >= rows or c < 0 or c >= cols:
            return 0

        if visited[r][c] or arr[r][c] == "X":
            return 0

        visited[r][c] = True
        size = 1

        size += dfs(r + 1, c)
        size += dfs(r - 1, c)
        size += dfs(r, c + 1)
        size += dfs(r, c - 1)
        return size

    max_size = 0
    for i in range(rows):
        for j in range(cols):
            if arr[i][j] == "O" and not visited[i][j]:
                max_size = max(max_size, dfs(i, j))

    return max_size


print(best_land(arr))
