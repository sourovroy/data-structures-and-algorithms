class Stack:

    def __init__(self):
        self.__list = []

    def push(self, value):
        self.__list.append(value)

    def pop(self):
        item = self.peek()
        del self.__list[-1]
        return item

    def peek(self):
        return self.__list[-1]

    def __len__(self):
        return len(self.__list)

    def is_empty(self):
        return len(self.__list) == 0

"""
stack = Stack()

stack.push(3)
stack.push(2)
stack.push(7)
stack.push(5)
print( len(stack) )
stack.pop()
print( stack.peek() )
print( len(stack) )
"""