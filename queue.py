class Query:

    def __init__(self):
        self.__list = []

    def enqueue(self, value):
        self.__list.append(value)

    def dequeue(self):
        item = self.__list[0]
        del self.__list[0]
        return item

    def front(self):
        return self.__list[0]

    def __len__(self):
        return len(self.__list)

que = Query()
que.enqueue(1)
que.enqueue(2)
que.enqueue(3)
print(len(que))
print(que.front())
que.dequeue()
print(que.front())
print(len(que))