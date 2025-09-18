T = int(input())

for _ in range(T):
    stack = []

    string = input()
    for i in range(len(string)):
        if stack and string[i] == ")" and stack[-1] == "(":
            stack.pop()
        else:
            stack.append(string[i])

    if not stack:
        print("YES")
    else:
        print("NO")
