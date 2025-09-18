M, N, L = map(int, input().split())
guns = list(map(int, input().split()))
guns.sort()
animals = []

for _ in range(N):
    animals.append((tuple(map(int, input().split()))))


def get_animal(gun, animal):
    return (abs(gun - animal[0]) + animal[1]) <= L


def get_closest_gun(animal):
    x, y = animal[0], animal[1]
    left, right = 0, len(guns) - 1
    closest = False

    while left <= right:
        mid = (left + right) // 2
        distance = abs(guns[mid] - x) + y

        if distance <= L:
            closest = mid
            break
        elif guns[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return closest


count = 0
for animal in animals:
    closest_gun = get_closest_gun(animal)
    if not closest_gun:
        continue
    if get_animal(guns[closest_gun], animal):
        count += 1

print(count)
