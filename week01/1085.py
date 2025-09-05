x, y, w, h = map(int, input().split())

minx = min(abs(x - w), abs(x))
miny = min(abs(y - h), abs(y))
print(min(minx, miny))
