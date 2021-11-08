class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""


def topView(root):
    from collections import deque
    q = deque()
    q.append((0, root))
    res, minCol, maxCol = dict(), 0, 0
    while len(q) > 0:
        col, node = q.popleft()
        if col < minCol:
            minCol = col
        if col > maxCol:
            maxCol = col
        if col not in res.keys():
            res[col] = node.info
        if node.left:
            q.append((col-1, node.left))
        if node.right:
            q.append((col+1, node.right))
    
    for key in range(minCol, maxCol+1):
        print(res[key], end=' ')


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)
