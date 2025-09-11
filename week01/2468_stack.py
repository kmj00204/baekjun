n = int(input())
land = [list(map(int, input().split())) for _ in range(n)]
max_num_of_safety = 0


def func(visited, height, start_i, start_j):
    visited[start_i][start_j] = True
    stack = []
    stack.append((start_i, start_j))

    while stack:
        i, j = stack.pop()
        for di, dj in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n:
                if not visited[ni][nj] and land[ni][nj] > height:
                    stack.append((ni, nj))
                    visited[ni][nj] = True


for height in range(101):
    visited = [[False for _ in range(n)] for _ in range(n)]
    num_of_safety = 0
    for i in range(n):
        for j in range(n):
            if land[i][j] > height and not visited[i][j]:
                func(visited, height, i, j)
                num_of_safety += 1
    max_num_of_safety = max(max_num_of_safety, num_of_safety)

print(max_num_of_safety)
