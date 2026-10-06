# Queue implementation using front and rear operations
'''
class Queue:
    def __init__(self, size):
        self.size = size
        self.front = -1
        self.rear = -1
        self.q = [None] * self.size

    def enqueue(self, val):
        # Queue is full
        if self.rear == self.size - 1:
            return "Queue is full"
        # Queue is empty
        if self.front == -1:
            self.front = 0
        self.rear += 1
        self.q[self.rear] = val
    def dequeue(self):
        if self.front == -1:
            return "Queue is empty"
        self.front += 1
        val = self.q[self.front]
        return val

    def display(self):
        if self.front == -1:
            print("Queue is empty")
            return
        for i in range(self.front,self.rear+1):
            print(self.q[i], end=" -> ")
        print()

q = Queue(5)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
q.dequeue()
q.display()

# Queue implementation using Linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Queue_LL:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self, val):
        new_node = Node(val)
        if self.front is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node
'''