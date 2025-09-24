import sys

sys.setrecursionlimit(1000000)

preorder = []
while True:
    try:
        preorder.append(int(input()))
    except:
        break


def postorder(preorder):
    if not preorder:
        return []
    root = preorder[0]
    left = [x for x in preorder[1:] if x < root]
    right = [x for x in preorder[1:] if x > root]

    return postorder(left) + postorder(right) + [root]


result = postorder(preorder)
for val in result:
    print(val)
