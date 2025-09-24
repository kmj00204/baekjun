from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
cost = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(N):
    arr.append(list(map(int, input().strip())))


def bfs(start_i, start_j, visited):
    que = deque()
    que.append((start_i, start_j))
    visited[start_i][start_j] = True
    while que:
        i, j = que.popleft()
        for di, dj in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and arr[ni][nj] > 0:
                que.append((ni, nj))
                if arr[ni][nj] > 1:
                    arr[ni][nj] = min(arr[ni][nj], arr[i][j] + 1)
                else:
                    arr[ni][nj] = arr[i][j] + 1
                visited[ni][nj] = True
    return arr[N - 1][M - 1]


visited = [[False for _ in range(M)] for _ in range(N)]
result = bfs(0, 0, visited)

print(result)
