import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))


def count_island():
    island = 0
    visited = [[False for _ in range(M)] for _ in range(N)]

    def dfs(start_i, start_j, visited):
        stack = [(start_i, start_j)]
        while stack:
            i, j = stack.pop()
            for di, dj in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
                ni, nj = i + di, j + dj
                if (
                    0 <= ni < N
                    and 0 <= nj < M
                    and not visited[ni][nj]
                    and arr[ni][nj] > 0
                ):
                    stack.append((ni, nj))
                    visited[ni][nj] = True

    for i in range(N):
        for j in range(M):
            if not visited[i][j] and arr[i][j] > 0:
                visited[i][j] = True
                dfs(i, j, visited)
                island += 1
                if island > 1:
                    return island

    return island


def year_pass():
    down = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            for di, dj in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] < 1:
                    down[i][j] += 1
    for i in range(N):
        for j in range(M):
            arr[i][j] -= down[i][j]


time = 0
while True:
    island = count_island()
    if island > 1:
        break
    year_pass()

    time += 1
    if all(x < 1 for row in arr for x in row):
        print(0)
        exit()

print(time)
