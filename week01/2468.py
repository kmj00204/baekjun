import sys

sys.setrecursionlimit(100000)

n = int(input())
land_input = [list(map(int, input().split())) for _ in range(n)]


def land_drawned(height):
    lands = land_input[:]
    for i in range(n):
        for j in range(n):
            if lands[i][j] <= height:
                lands[i][j] = False
    return lands


def dfs(land, visited, i, j):
    if i < 0 or i >= n or j < 0 or j >= n:
        return 0

    if visited[i][j] == True:
        return 0
    if land[i][j] == False:
        return 0

    visited[i][j] = True

    if land[i][j] == False:
        zone = 0
    else:
        zone = 1

    zone += dfs(land, visited, i + 1, j)
    zone += dfs(land, visited, i - 1, j)
    zone += dfs(land, visited, i, j + 1)
    zone += dfs(land, visited, i, j - 1)
    return zone


def main():
    max_num = 0
    for height in range(101):
        num_of_safety = 0
        land = land_drawned(height)
        visited = [[False for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if not visited[i][j] and land[i][j] != False:
                    if dfs(land, visited, i, j) > 0:
                        num_of_safety += 1
        max_num = max(max_num, num_of_safety)

    print(max_num)


main()
