def factorial(n):
    if n == 1 or n == 2:
        return n
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


n = int(input())
print(factorial(n))
