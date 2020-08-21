class Node:
    def __init__(self, value):
        self.prev = None
        self.next = None
        self.value = value

class DubbleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.size += 1

    def remove(self, value):
        node = self.head
        while node is not None:
            if node.value == value:
                self.__remove_node(node)
            node = node.next

    def __remove_node(self, node):
        if node.prev is None:
            self.head = node.next
            self.head.prev = None
        elif node.next is None:
            self.next = node.prev
            self.next.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.size -= 1

    def __str__(self):
        values = []
        node = self.head
        while node is not None:
            values.append(node.value)
            node = node.next

        items = ", ".join(str(value) for value in values)
        return f"[{items}]"

linked = DubbleLinkedList()
linked.add(1)
linked.add(3)
linked.add(5)
linked.add(7)
linked.add(8)

print(linked)
print(linked.size)

linked.remove(5)
print(linked)

linked.remove(1)
print(linked)

linked.remove(3)
print(linked)

print(linked.size)