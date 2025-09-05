def Prime_Number_Less_Or_Equal(number):
    if number < 2:
        return False
    arr = [i for i in range(number + 1)]

    for n in arr:
        if n == 0 or n == 1 or n == False:
            continue
        for i in range(n * 2, number + 1, n):
            arr[i] = False
    return [item for item in arr if item != False and item != 1]


n = int(input())
for _ in range(n):
    number = int(input())
    arr = Prime_Number_Less_Or_Equal(number)
    answer = []
    for prime in arr:
        if number - prime in arr and prime <= number - prime:
            answer.append((prime, number - prime))
    if len(answer) == 1:
        print(f"{answer[0][0]} {answer[0][1]}")
    else:
        minnumber = number
        minidx = None
        for idx, (a, b) in enumerate(answer):
            if minnumber > abs(a - b):
                minnumber = abs(a - b)
                minidx = idx
        print(f"{answer[minidx][0]} {answer[minidx][1]}")
