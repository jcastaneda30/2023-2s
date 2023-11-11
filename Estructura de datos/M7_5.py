import math

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursively(self.root, key)

    def _insert_recursively(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self._insert_recursively(root.left, key)
        elif key > root.key:
            root.right = self._insert_recursively(root.right, key)
        return root

    def inorder(self, h):
        return    self._inorder_recursively(self.root, 1, h)

    def _inorder_recursively(self, root, level, h):
        l=0
        r=0
        if root:
            l = self._inorder_recursively(root.right, level + 1, h)
            r = self._inorder_recursively(root.left, level + 1, h)
            if level == h:
                return 1
        return l+r

C = int(input())
for i in range(C):
    valores = [int(x) for x in input().split() if int(x) >= 0]
    bst = BinarySearchTree()
    for i in valores:
        bst.insert(i)
    logaritmo = math.ceil(math.log2(len(valores) + 1))
    waos = bst.inorder(logaritmo)
    if(waos==2**(logaritmo-1) ):print("completo")
    else: print("no")
