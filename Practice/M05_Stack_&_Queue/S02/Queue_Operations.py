#Queue implementation using front and rear pointers
class Queue:
    def __init__(self,size):
        self.size = size
        self.front = -1
        self.rear = -1
        self.q = [None]*self.size
    def enqueue(self,data):
        if self.rear == self.size-1:
            return "Queue is full"
        self.rear += 1
        self.q[self.rear] = val
    def dequeue(self):
        pass