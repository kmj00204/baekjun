from collections import deque

n, k = map(int, input().split())

queue = deque()
answer = []

for i in range(n):
    queue.append(i + 1)

i = 1
while queue:
    if i != 0 and i % k == 0:
        answer.append(queue.popleft())
    else:
        queue.append(queue.popleft())
    i += 1

print(f"<{', '.join(map(str,answer))}>")
