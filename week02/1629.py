a, b, c = map(int, input().split())


def func(a, b, c):
    result = 1
    a = a % c
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % c
        a = (a * a) % c
        b //= 2
    return result


print(func(a, b, c))
