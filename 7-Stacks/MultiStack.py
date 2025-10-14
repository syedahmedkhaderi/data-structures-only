"""
MultiStack - Three Stacks in One Array

Instead of making 3 separate arrays, we use ONE big array and split it into 3 parts.
Each part works like its own stack.

Example with stacksize=3:
Array: [0, 1, 2, 3, 4, 5, 6, 7, 8]
       |Stack 0| |Stack 1| |Stack 2|

Stack 0 uses: 0, 1, 2
Stack 1 uses: 3, 4, 5
Stack 2 uses: 6, 7, 8
"""

class MultiStack:

    def __init__(self, stacksize):
        """
        Create 3 stacks in one array.
        
        stacksize: How many items each stack can hold
        
        Example: If stacksize = 2
        - array = [0, 0, 0, 0, 0, 0]  (2 * 3 = 6 spots total)
        - sizes = [0, 0, 0]  (all stacks start empty)
        - Stack 0 gets spots 0-1
        - Stack 1 gets spots 2-3
        - Stack 2 gets spots 4-5
        """
        self.numstacks = 3  # We have 3 stacks
        self.array = [0] * (stacksize * self.numstacks)  # One big array for all stacks
        self.sizes = [0] * self.numstacks  # How many items in each stack
        self.stacksize = stacksize  # Max items per stack
        # print(self.array)
        # print(self.sizes)

    def Push(self, item, stacknum):
        """
        Add an item to a stack.
        
        item: What to add
        stacknum: Which stack (0, 1, or 2)
        
        Example: Push(10, 0) adds 10 to stack 0
        """
        if self.IsFull(stacknum):
            raise Exception('Stack is full')
        self.sizes[stacknum] += 1  # Add 1 to the count
        self.array[self.IndexOfTop(stacknum)] = item  # Put item in the right spot

    def Pop(self, stacknum):
        """
        Remove and return the top item from a stack.
        
        stacknum: Which stack (0, 1, or 2)
        
        Example: If stack 0 has [5, 10, 15]
        - Pop(0) returns 15
        - Stack 0 now has [5, 10]
        """
        if self.IsEmpty(stacknum):
            raise Exception('Stack is empty')
        value = self.array[self.IndexOfTop(stacknum)]  # Get the top item
        self.array[self.IndexOfTop(stacknum)] = 0  # Clear that spot
        self.sizes[stacknum] -= 1  # Reduce the count by 1
        return value

    def Peek(self, stacknum):
        """
        Look at the top item without removing it.
        
        stacknum: Which stack (0, 1, or 2)
        
        Example: If stack 1 has [20, 30, 40]
        - Peek(1) returns 40
        - Stack stays the same: [20, 30, 40]
        """
        if self.IsEmpty(stacknum):
            raise Exception('Stack is empty')
        return self.array[self.IndexOfTop(stacknum)]  # Just look, don't remove

    def IsEmpty(self, stacknum):
        """
        Check if a stack is empty.
        
        stacknum: Which stack (0, 1, or 2)
        Returns: True if empty, False if it has items
        
        Example: If sizes = [0, 2, 1]
        - IsEmpty(0) → True  (stack 0 is empty)
        - IsEmpty(1) → False (stack 1 has 2 items)
        """
        return self.sizes[stacknum] == 0

    def IsFull(self, stacknum):
        """
        Check if a stack is full.
        
        stacknum: Which stack (0, 1, or 2)
        Returns: True if full, False if there's space
        
        Example: If stacksize = 3 and sizes = [3, 1, 0]
        - IsFull(0) → True  (stack 0 has 3/3 items - full!)
        - IsFull(1) → False (stack 1 has 1/3 items)
        """
        return self.sizes[stacknum] == self.stacksize

    def IndexOfTop(self, stacknum):
        """
        Find where the top of a stack is in the array.
        
        This is the KEY method! It figures out the correct array position.
        
        How it works:
        1. Find where the stack starts: stacknum * stacksize
        2. Add how many items are in it: + sizes[stacknum]
        3. Go back one spot (because arrays start at 0): - 1
        
        Example with stacksize = 3:
        Array: [0, 1, 2, 3, 4, 5, 6, 7, 8]
               |Stack 0| |Stack 1| |Stack 2|
        
        Stack 0 (stacknum=0):
        - Starts at: 0 * 3 = 0
        - If it has 2 items: 0 + 2 - 1 = 1
        - Top is at position 1
        
        Stack 1 (stacknum=1):
        - Starts at: 1 * 3 = 3
        - If it has 3 items: 3 + 3 - 1 = 5
        - Top is at position 5
        
        Stack 2 (stacknum=2):
        - Starts at: 2 * 3 = 6
        - If it has 1 item: 6 + 1 - 1 = 6
        - Top is at position 6
        
        Step-by-step example:
        Start: array = [0, 0, 0, 0, 0, 0, 0, 0, 0], sizes = [0, 0, 0]
        
        Push(10, 0), Push(20, 0):
        array = [10, 20, 0, 0, 0, 0, 0, 0, 0], sizes = [2, 0, 0]
        IndexOfTop(0) = 0 + 2 - 1 = 1 (points to 20)
        
        Push(30, 1), Push(40, 1), Push(50, 1):
        array = [10, 20, 0, 30, 40, 50, 0, 0, 0], sizes = [2, 3, 0]
        IndexOfTop(1) = 3 + 3 - 1 = 5 (points to 50)
        
        Push(60, 2):
        array = [10, 20, 0, 30, 40, 50, 60, 0, 0], sizes = [2, 3, 1]
        IndexOfTop(2) = 6 + 1 - 1 = 6 (points to 60)
        """
        offset = stacknum * self.stacksize  # Where does this stack start?
        return offset + self.sizes[stacknum] - 1  # Add items count, minus 1 for array indexing


print("Creating a MultiStack with stacksize=3 (each stack can hold 3 items)")
stack = MultiStack(3)

# Adding items to Stack 0
stack.Push(10, 0)
stack.Push(20, 0)
stack.Push(30, 0)

# Adding items to Stack 1
stack.Push(100, 1)
stack.Push(200, 1)

# Adding items to Stack 2
stack.Push(1000, 2)

print(f"Top of Stack 0: {stack.Peek(0)}")  # Should be 30
print(f"Top of Stack 1: {stack.Peek(1)}")  # Should be 200
print(f"Top of Stack 2: {stack.Peek(2)}")  # Should be 1000

print(f"Popped from Stack 0: {stack.Pop(0)}")  # Removes and returns 30
print(f"Popped from Stack 1: {stack.Pop(1)}")  # Removes and returns 200
print(f"New top of Stack 0: {stack.Peek(0)}")  # Should be 20

print(f"Is Stack 0 empty? {stack.IsEmpty(0)}")  # False (has 2 items)
print(f"Is Stack 0 full? {stack.IsFull(0)}")    # False (has 2/3 items)
print(f"Is Stack 2 full? {stack.IsFull(2)}")    # False (has 1/3 items)

stack.Push(2000, 2)
stack.Push(3000, 2)
print(f"Is Stack 2 full now? {stack.IsFull(2)}")  # True (has 3/3 items)


"""
RAISE     → Stop the program and show an error
EXCEPTION → The error message you create
YIELD     → Return a value but keep the function alive for next time

In MultiStack:
- We use RAISE and EXCEPTION to prevent errors (like adding to a full stack)
- We don't use YIELD in this code (but now you know what it does!)
"""