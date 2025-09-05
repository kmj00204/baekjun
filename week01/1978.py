def isPrimary(number):
    if number < 2:
        return False
    for i in range(2, int(number ** (0.5)) + 1):
        if number % i == 0:
            return False
    return True


n = int(input())
score = 0
arr = map(int, input().split())

for number in arr:
    if isPrimary(number):
        score += 1
print(score)
