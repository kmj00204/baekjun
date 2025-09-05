def isHansu(number):
    numstr = str(number)
    if len(numstr) == 1:
        return True
    diff = int(numstr[0]) - int(numstr[1])
    for i in range(1, len(numstr) - 1):
        if diff != int(numstr[i]) - int(numstr[i + 1]):
            return False
    return True


n = int(input())
answer = 0

for i in range(1, n + 1):
    if isHansu(i):
        answer += 1
print(answer)
