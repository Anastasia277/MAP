import random
from collections import deque

# Structura unui nod in arborele binar
class Node:
    def __init__(self, key): 
        self.left = None 
        self.right = None 
        self.val = key 

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

# Traversare pre-ordine
def preorder(root):
    if root:
        print(root.val, end=" ")
        preorder(root.left)
        preorder(root.right)

# Traversare in-ordine
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

# Traversare post-ordine
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=" ")

# Traversare pe niveluri 
def level_order(root):
    if root is None:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.val, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Functia de afisare a arborelui binar 
def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.val))
        if root.left or root.right:  # Doar dacă are copii
            if root.left:
                print_tree(root.left, level + 1, "L--- ")
            else:
                print(" " * ((level + 1) * 4) + "L--- None")
            if root.right:
                print_tree(root.right, level + 1, "R--- ")
            else:
                print(" " * ((level + 1) * 4) + "R--- None")

def build_random_tree(num_elements, min_value, max_value):
    root = None
    for _ in range(num_elements):
        key = random.randint(min_value, max_value)
        root = insert(root, key)
    return root

root = build_random_tree(5, 1, 10)


print("Arborele binar:")
print_tree(root)

print("Pre-ordine:")
preorder(root)
print("\nIn-ordine:")
inorder(root)
print("\nPost-ordine:")
postorder(root)
print("\nPe nivel:")
level_order(root)
