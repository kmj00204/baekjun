a, b, c = [int(input()) for _ in range(3)]

num = a * b * c

numstr = str(num)

for i in range(10):
    number = 0
    for j in range(len(numstr)):
        if int(numstr[j]) == i:
            number += 1
    print(number)
