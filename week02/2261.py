n = int(input())

points = []
dp = [0 for _ in range(n)]

for _ in range(n):
    points.append(tuple(map(int, input().split())))

points.sort(key=lambda x: (x[0], x[1]))

print("pass")
