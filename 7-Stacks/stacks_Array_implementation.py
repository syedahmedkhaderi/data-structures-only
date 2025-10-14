class Stack:
    def __init__(self):
        self.arr = []

    def peek(self):
        return self.arr[len(self.arr) - 1]

    def push(self, value):
        self.arr.append(value)
        return

    def pop(self):
        if len(self.arr):
            self.arr.pop()
            return
        else:
            print("Empty Stack")
            return

    def is_empty(self):
        if not len(self.arr):
            return "Empty"
        return "Not Empty"
#Stack follows LIFO, so for the print operation, we have to print the last element of the list first.
#This will require a loop traversing the entire array, so the complexity is O(n)
    def print_stack(self):
        for i in range(len(self.arr)-1, -1, -1):
            print(self.arr[i])
        return
    def clear(self):
        self.items = []
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        values = [str(x) for x in reversed(self.list)]
        return '\n'.join(values)
    

my_stack = Stack()
my_stack.push("Syed")
my_stack.push("Courses")
my_stack.push("Are")
my_stack.push("Awesome")
my_stack.print_stack()
#Awesome
#Are
#Courses
#Syed

my_stack.pop()
my_stack.pop()
my_stack.print_stack()
#Courses
#Syed

print(my_stack.peek())
#Courses

print(my_stack.__dict__)
#{'array': ["Syed", 'Courses']}

print(my_stack) # Print the stack (from top to bottom)