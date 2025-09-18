n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

white = 0
black = 0


def func(n, r, c):
    global white, black

    if all((arr[i][j] == 1 for i in range(r, r + n) for j in range(c, c + n))):
        black += 1
        return

    if all((arr[i][j] == 0 for i in range(r, r + n) for j in range(c, c + n))):
        white += 1
        return

    half = n // 2

    func(half, r, c)
    func(half, r + half, c)
    func(half, r, c + half)
    func(half, r + half, c + half)


func(n, 0, 0)

print(white)
print(black)
