num = int(input())

for _ in range(num):
    str = input()
    idx = -1
    total = 0
    while idx >= -1 * len(str):
        if str[idx] == "O":
            j = idx
            score = 0
            while j >= -1 * len(str):
                if str[j] == "O":
                    score += 1
                    j -= 1
                else:
                    break

            total += score
        idx -= 1
    print(total)
