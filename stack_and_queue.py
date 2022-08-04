"""
The purpose of this project is to illustrate the concept of stack and queue
1. stack (view it as a drinking beer)
         LIFO (Last in first out)
    1.1: push
        this function is going to add an element on the top of stack
    1.2: pop
        this function is going to remove an element on the top of the stack
2. queue (view it as a waiting line)
         FIFO (First in first out)
    2.1: enqueue

    2.2: dequeue

"""
class ArrayStack:
    def __init__(self):
        self._data = []
    def push(self, val):
        self._data.append(val)
        print(f"The data {val} has been added.")
    def pop(self):
        remove_num = self._data.pop()
        print(f"The data {remove_num} has been removed.")
    def get_current_data(self):
        print(self._data)
stack = ArrayStack()
print("This is the case of stack:")
stack.push(1)
stack.push(2)
stack.push(3)
stack.get_current_data()
stack.pop()
stack.get_current_data()
#------------------------#
print()
#------------------------#
class ArrayQueue:
    def __init__(self):
        self._data = []
    def enqueue(self, val):
        self._data.append(val)
        print(f"The data {val} has been added.")
    def dequeue(self):
        remove_num = self._data[0]
        self._data = self._data[1:]
        print(f"The data {remove_num} has been removed.")
    def get_current_data(self):
        print(self._data)
queue = ArrayQueue()
print("This is the case of queue:")
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.get_current_data()
queue.dequeue()
queue.get_current_data()
