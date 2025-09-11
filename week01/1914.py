n = int(input())


def hannoi(n):
    if n == 1:
        return 1
    return 1 + hannoi(n - 1) * 2


def show_hannoi(n, a, b):
    c = 6 - a - b
    if n == 1:
        print(a, b)
    else:
        show_hannoi(n - 1, a, c)
        print(a, b)
        show_hannoi(n - 1, c, b)


answer = hannoi(n)
print(answer)
if n <= 20:
    show_hannoi(n, 1, 3)
