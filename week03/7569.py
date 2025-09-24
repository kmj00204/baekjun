import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[False] * M for _ in range(N)] for _ in range(H)]

queue = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1:
                queue.append((i, j, k))


def bfs():
    while queue:
        z, y, x = queue.popleft()
        for dx, dy, dz in [
            (1, 0, 0),
            (-1, 0, 0),
            (0, 1, 0),
            (0, -1, 0),
            (0, 0, 1),
            (0, 0, -1),
        ]:
            nx = x + dx
            ny = y + dy
            nz = z + dz

            if nx < 0 or nx >= M or ny < 0 or ny >= N or nz < 0 or nz >= H:
                continue

            if box[nz][ny][nx] == 0 and not visited[nz][ny][nx]:
                visited[nz][ny][nx] = True
                box[nz][ny][nx] = box[z][y][x] + 1
                queue.append((nz, ny, nx))


bfs()

tomato_max = 0
for i in box:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        tomato_max = max(tomato_max, max(j))

print(tomato_max - 1)
