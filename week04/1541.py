import sys

input = sys.stdin.readline

L = input().strip()

a = L.split("-")


ans = 0
b = a[0].split("+")
ans = sum(map(int, b))

for item in a[1:]:
    b = item.split("+")
    tmp = sum(map(int, b))
    ans -= tmp


print(ans)
