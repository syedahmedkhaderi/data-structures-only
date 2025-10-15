"""Circular, capacity-aware queue implementation.

This data structure preallocates storage and reuses slots via wrap-around indexes.
Compared to ``QueueNoSize`` (which grows an unbounded Python list and uses
``pop(0)`` with O(n) cost), this version:
- keeps enqueue/dequeue operations at O(1) time by avoiding list shifting,
- prevents accidental memory blow-ups by enforcing a maximum size,
- makes the queue's performance predictable for systems with tight constraints.
"""


class Queue:
    def __init__(self, maxSize):
        # Preallocate the array so enqueue/dequeue never trigger costly resizes.
        self.items = maxSize * [None]
        self.maxSize = maxSize
        # ``start`` points to the front item, ``top`` to the rear; both wrap around.
        self.start = -1
        self.top = -1
    
    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.maxSize:
            return True
        else:
            return False
    
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
    
    def enqueue(self, value):
        if self.isFull():
            return "The queue is full"
        else:
            if self.top + 1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
            return "The element is inserted at the end of Queue"
    
    def dequeue(self):
        if self.isEmpty():
            return "There is not any element in the Queue"
        else:
            firstElement = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.maxSize:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return firstElement
    
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the Queue"
        else:
            return self.items[self.start]
    
    def delete(self):
        self.items = self.maxSize * [None]
        self.top = -1
        self.start = -1


customQueue = Queue(3)
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.delete()
print(customQueue)