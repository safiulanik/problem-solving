class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


def preOrder(root):
    if root == None:
        return
    print(root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    #Node is defined as
    #self.left (the left child of the node)
    #self.right (the right child of the node)
    #self.info (the value of the node)

    def insert(self, val, root=None):
        #Enter you code here.
        node = Node(val)
        if self.root is None:
            self.root = node
            return self.root

        if root is None:
            root = self.root

        if val < root.info:
            if root.left is None:
                root.left = node
            else:
                self.insert(val, root.left)
        else:
            if root.right is None:
                root.right = node
            else:
                self.insert(val, root.right)

        return self.root


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)


"""
Testcase 1:
6
4 2 3 1 7 6
"""
