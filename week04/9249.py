import sys

input = sys.stdin.readline

A = list(map(ord, input().strip()))
B = list(map(ord, input().strip()))

# A = list(input().strip())
# B = list(input().strip())


def find(longer, shorter, idx):
    target = shorter[idx][0]

    def lower_bound():
        left, right = 0, len(longer)
        while left < right:
            mid = (left + right) // 2
            if longer[mid][0] < target:
                left = mid + 1
            else:
                right = mid
        return left

    def upper_bound():
        left, right = 0, len(longer)
        while left < right:
            mid = (left + right) // 2
            if longer[mid][0] <= target:
                left = mid + 1
            else:
                right = mid
        return left

    l = lower_bound()
    r = upper_bound()

    if l == r:
        return False, False

    return l, r - 1


def how_long(longer, shorter, target, idx):
    res = 0
    idx_long = 0
    idx_short = 0

    len_longer = len(longer[target])
    len_shorter = len(shorter[idx])

    while idx_long < len_longer and idx_short < len_shorter:
        if longer[target][idx_long] == shorter[idx][idx_short]:
            res += 1
        idx_long += 1
        idx_short += 1

    return res


arr_A = []
arr_B = []

for i in range(len(A)):
    arr_A.append(A[i:])

for i in range(len(B)):
    arr_B.append(B[i:])


longer = arr_A if len(arr_A) >= len(arr_B) else arr_B
shorter = arr_A if len(arr_A) < len(arr_B) else arr_B
longer.sort()

max_val = 0
max_idx = False

idx = 0

while idx < len(shorter):
    start, end = find(longer, shorter, idx)
    if start is False or end is False:
        idx += 1
        continue

    while start <= end:
        tmp = how_long(longer, shorter, start, idx)
        if tmp > max_val:
            max_val = tmp
            max_idx = idx
        start += 1
    idx += 1

result = shorter[max_idx][:max_val]

print(max_val)
print("".join(map(chr, result)))
