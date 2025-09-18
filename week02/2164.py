from collections import deque

queue = deque()

n = int(input())
for i in range(n):
    queue.append(i + 1)

while len(queue) > 2:
    a = queue.popleft()
    b = queue.popleft()
    queue.append(b)
print(queue.pop())
