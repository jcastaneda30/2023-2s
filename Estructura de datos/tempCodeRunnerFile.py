
# Ejemplo de aplicacion
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)

print(bst.search(7))  # True
print(bst.search(9))  # False

print(bst.inorder())  # [3, 5, 7, 10, 15]

bst.delete(5)
print(bst.inorder())  # [3, 7, 10, 15]