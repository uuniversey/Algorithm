def preorder(s):
    if not s == '.':
        print(s, end='')
        preorder(tree[s][0])
        preorder(tree[s][1])


def inorder(s):
    if not s == '.':
        inorder(tree[s][0])
        print(s, end='')
        inorder(tree[s][1])


def postorder(s):
    if not s == '.':
        postorder(tree[s][0])
        postorder(tree[s][1])
        print(s, end='')


N = int(input())
tree = {}
for _ in range(N):
    root, left, right = input().split()
    tree[root] = [left, right]

preorder('A')
print()
inorder('A')
print()
postorder('A')