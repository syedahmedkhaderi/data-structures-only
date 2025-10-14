class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    # Added this so we could view the stack in easier and more readable format.
    def __str__(self):
        arr = []
        curr = self.top
        while curr:
            arr.append(curr.value)
            curr = curr.next
        return f"Stack(top -> bottom): {arr}, length: {self.length}"

    def peek(self):
        return self.top.value if self.top else None

    def push(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.top = new_node
            self.bottom = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1
        return self

    def pop(self):
        if not self.top:
            self.bottom = None
            return None
        else:
            self.top = self.top.next
            self.length -= 1
            if self.length == 0:
                self.bottom = None

    def is_empty(self):
        if self.length == 0:
            return "Stack is Empty"
        else:
            return "Not Empty"

    def print_stack(self):
        if self.top is None:
            print("Stack empty")
        else:
            current_pointer = self.top
            while current_pointer is not None:
                print(current_pointer.value)
                current_pointer = current_pointer.next
    
    def size(self):
        return self.length

    def clear(self):
        self.bottom = None
        self.top = None
        self.length = 0

my_stack = Stack()
print(my_stack.peek())
#None

my_stack.push('google')
my_stack.push('udemy')
my_stack.push('discord')
my_stack.print_stack()
#discord
#udemy
#google

print(my_stack.top.data)
#discord

print(my_stack.bottom.data)
#gogle

my_stack.pop()
my_stack.print_stack()
#udemy
#google

my_stack.pop()
my_stack.pop()
my_stack.print_stack()
#Stack Empty