stack = []
size = 0


n = int(input())
for _ in range(n):
    command = input().split()
    if len(command) > 1:
        stack.append(command[1])
        size += 1
    else:
        if command[0] == "top":
            if size == 0:
                print("-1")
            else:
                print(stack[-1])

        if command[0] == "size":
            print(size)

        if command[0] == "empty":
            print(1 if size == 0 else 0)

        if command[0] == "pop":
            if size == 0:
                print("-1")
            else:
                print(stack.pop())
                size -= 1
