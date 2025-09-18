import sys

input = sys.stdin.readline

queue = []
start = 0
finish = 0

n = int(input())
for _ in range(n):
    command = input().split()
    if len(command) > 1:
        queue.append("")
        queue[finish] = command[1]
        finish += 1
    if command[0] == "pop":
        if finish == start:
            print(-1)
        else:
            print(queue[start])
            start += 1
    if command[0] == "size":
        print(finish - start)
    if command[0] == "empty":
        print(1 if not finish - start else 0)
    if command[0] == "front":
        if finish == start:
            print(-1)
        else:
            print(queue[start])
    if command[0] == "back":
        if finish == start:
            print(-1)
        else:
            print(queue[finish - 1])
