from stack import Stack
from BinaryTreePrinter import BinaryTreePrinter

class Node:

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.__insert_value(self.root, value)

    def __insert_value(self, node, value):
        if node.value == value:
            return

        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self.__insert_value(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self.__insert_value(node.right, value)

    def __str__(self):
        printer = BinaryTreePrinter()
        return printer.get_tree_string(self.root)

    # DFS Implementation
    def contains_dfs(self, value):
        nodes = Stack()
        nodes.push(self.root)

        while not nodes.is_empty():
            current = nodes.pop()
            # print(current.value)
            if current.value == value:
                return True

            if value < current.value:
                if current.left is not None:
                    nodes.push(current.left)
            else:
                if current.right is not None:
                    nodes.push(current.right)

        return False

tree = BinarySearchTree()

tree.insert(10)

for i in [3, 6, 1, 8, 12, 15, 18, 7, 9]:
    tree.insert(i)

print(tree)

print("Contains 7: ", tree.contains_dfs(7))