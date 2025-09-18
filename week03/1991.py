n = int(input())
tree = {}

for _ in range(n):
    root, left, right = input().split()
    tree[root] = [left, right]

print(tree)
