n = int(input())

arr = [0] * n


def isClear(x):
    for i in range(x):
        if arr[x] == arr[i] or abs(arr[x] - arr[i]) == abs(x - i):
            return False
    return True


def n_queens(x):
    if x == n:
        return 1

    count = 0
    for i in range(n):
        arr[x] = i
        if isClear(x):
            count += n_queens(x + 1)
    return count


print(n_queens(0))
