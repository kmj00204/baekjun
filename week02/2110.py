n, c = map(int, input().split())
x = []

for _ in range(n):
    x.append(int(input()))
x.sort()


def can_put_gongyugi(distance):
    last_gongyugi = 0
    count = 1

    for i in range(1, n):
        if x[i] - x[last_gongyugi] >= distance:
            last_gongyugi = i
            count += 1
            if count >= c:
                return True

    return False


left = 0
right = 1000000000

while left <= right:
    mid = (left + right) // 2
    if can_put_gongyugi(mid):
        left = mid + 1
    else:
        right = mid - 1

print(right)
