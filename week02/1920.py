n = int(input())
N = set(map(int, input().split()))
m = int(input())
M = list(map(int, input().split()))

for num in M:
    if num in N:
        print(1)
    else:
        print(0)
