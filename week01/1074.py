n, r, c = map(int, input().split())


def fun(n, r, c):
    if n == 0:
        return 0
    half = 2 ** (n - 1)

    if r < half and c < half:
        return fun(n - 1, r, c)
    if r < half and c >= half:
        return half * half + fun(n - 1, r, c - half)
    if r >= half and c < half:
        return 2 * half * half + fun(n - 1, r - half, c)
    if r >= half and c >= half:
        return 3 * half * half + fun(n - 1, r - half, c - half)


print(fun(n, r, c))
