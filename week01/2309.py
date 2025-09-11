short_man = [int(input()) for _ in range(9)]
selected = []


def func(depth, index):
    if depth == 7:
        if sum(selected) == 100:
            for height in sorted(selected):
                print(height)
            exit()
        return

    for i in range(index, len(short_man)):
        selected.append(short_man[i])
        func(depth + 1, i + 1)
        selected.pop()


func(0, 0)
