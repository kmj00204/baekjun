import sys

input = sys.stdin.readline
N, K = map(int, input().split())
arr = list(map(int, input().split()))
numbers = {}

for i in range(K):
    if arr[i] not in numbers:
        numbers[arr[i]] = [i]
    else:
        numbers[arr[i]].append(i)

cnt = 0
container = set()
i = 0


def find_out(num):
    global cnt
    cnt += 1
    tmp = 0
    for item in container:
        target = min((a for a in numbers[item] if a > num), default=False)
        if target == False:
            container.remove(item)
            return False
        tmp = max(tmp, target)
    return tmp


while i < K:
    if len(container) == N and not arr[i] in container:
        number = find_out(i)
        if number == False:
            continue
        try:
            container.remove(arr[number])
        except:
            container.pop()

    container.add(arr[i])
    i += 1

print(cnt)
