from queue import Queue
from BinaryTreePrinter import BinaryTreePrinter

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return

        nodes = Queue()
        nodes.enqueue(self.root)

        while True:
            checking_node = nodes.dequeue()

            if checking_node.left is None:
                checking_node.left = Node(value)
                return

            if checking_node.right is None:
                checking_node.right = Node(value)
                return

            nodes.enqueue(checking_node.left)
            nodes.enqueue(checking_node.right)

    def __str__(self):
        printer = BinaryTreePrinter()
        return printer.get_tree_string(self.root)

    # BFS Implementation
    def contains(self, value):
        nodes = Queue()
        nodes.enqueue(self.root)

        while not nodes.is_empty():
            current = nodes.dequeue()
            # print(current.value)
            if current.value == value:
                return True

            if current.left is not None:
                nodes.enqueue(current.left)

            if current.right is not None:
                nodes.enqueue(current.right)

        return False

tree = BinaryTree()

tree.insert('a')
tree.insert('b')
tree.insert('c')
tree.insert('d')
tree.insert('e')
tree.insert('f')
tree.insert('g')

print(tree)
print()
print("Contains f: ", tree.contains("f"))