N, M = map(int, input().split())
trees = list(map(int, input().split()))
answer = []


def get_namu(height):
    namu = 0
    for tree in trees:
        if tree > height:
            namu += tree - height
    return namu


left = 0
right = 2000000000

while left <= right:
    mid = (left + right) // 2
    namu = get_namu(mid)

    if namu == M:
        print(mid)
        break
    if namu < M:
        right = mid - 1
    if namu > M:
        left = mid + 1
        answer.append(mid)

else:
    print(max(answer))
