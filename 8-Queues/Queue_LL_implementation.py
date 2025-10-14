class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        if self.first is None:
            return None
        return self.first.value

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.last = new_node
            self.first = self.last
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return

    def dequeue(self):
        if self.first is None:
            return None
        if self.last == self.first:
            self.last = None
        self.first = self.first.next
        self.length -= 1

    def print_queue(self):
        if self.length == 0:
            print("Queue Empty")
            return
        else:
            current_pointer = self.first
            while current_pointer is not None:
                if current_pointer.next is None:
                    print(current_pointer.value)
                else:
                    print(f'{current_pointer.value}  <<--  ', end='')
                current_pointer = current_pointer.next
            return


q = Queue()
print(q.peek())
q.enqueue('syed')
q.enqueue('Ahmed')
q.enqueue("khaderi")
q.print_queue()
print(q.peek())
q.dequeue()
q.dequeue()
q.print_queue()