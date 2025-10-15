class Queue:
    # Relies on list.pop(0), so every dequeue shifts all elements and becomes O(n) as the unlimited queue grows
    # Stores queue values in a Python list without a predefined size limit
    def __init__(self):
        self.items = []
    
    # Returns a space separated representation of the queue
    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    # Checks whether the queue currently holds any elements
    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False
    
    # Inserts a new value at the logical end of the queue
    def enqueue(self, value):
        self.items.append(value)
        return "The element is inserted at the end of Queue"
    
    # Removes and returns the front element by shifting underlying list left
    def dequeue(self):
        if self.isEmpty():
            return "The is not any element in the Queue"
        else:
            return self.items.pop(0)
    
    # Returns the front element without removing it
    def peek(self):
        if self.isEmpty():
            return "The is not any element in the Queue"
        else:
            return self.items[0]
    
    # Clears the queue by dropping the backing list reference
    def delete(self):
        self.items = None




# Example usage showing enqueue, peek, and delete operations
customQueue = Queue()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue.peek())
customQueue.delete()
