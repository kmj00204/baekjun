letter = list(input())

stack = []
answer = 0
tmp = 1

for i in range(len(letter)):

    if letter[i] == "(":
        stack.append(letter[i])
        tmp *= 2

    elif letter[i] == "[":
        stack.append(letter[i])
        tmp *= 3

    elif letter[i] == ")":
        if not stack or stack[-1] == "[":
            answer = 0
            break
        if letter[i - 1] == "(":
            answer += tmp
        stack.pop()
        tmp //= 2

    else:
        if not stack or stack[-1] == "(":
            answer = 0
            break
        if letter[i - 1] == "[":
            answer += tmp

        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(answer)
