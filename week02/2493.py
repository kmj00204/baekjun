n = int(input())

towers = list(map(int, input().split()))
stack = []
answer = [0 for _ in range(n)]

for i in range(n):
    while stack and towers[stack[-1]] < towers[i]:
        stack.pop()  # 나 이전의 나보다 작은놈은 필요 x

    if stack:
        answer[i] = stack[-1] + 1  # 기록할때 +1하기 (0번은 안셈)

    stack.append(i)


print(" ".join(map(str, answer)))
