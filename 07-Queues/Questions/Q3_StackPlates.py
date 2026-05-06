#   Created by Elshad Karimov on 02/06/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

# Stack of Plates

class PlateStack():
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []
    
    def __str__(self):
        return self.stacks
    
    def push(self, item):
        if len(self.stacks) > 0 and (len(self.stacks[-1])) < self.capacity:
            self.stacks[-1].append(item)
        else:
            self.stacks.append([item])
    
    def pop(self):
        while len(self.stacks) and len(self.stacks[-1]) == 0:
            self.stacks.pop()
        if len(self.stacks) == 0:
            return None
        else:
            return self.stacks[-1].pop()
    
    def pop_at(self, stackNumber):
        if len(self.stacks[stackNumber]) > 0:
            return self.stacks[stackNumber].pop()
        else:
            return None


customStack= PlateStack(2)
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
print(customStack.pop_at(1))

'''
class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stack = []
        

    def push(self, val: int) -> None:
        for i in range(len(self.stack)):
            if len(self.stack[i]) < self.capacity:
                self.stack[i].append(val)
                return
        
        self.stack.append([val])
        

    def pop(self) -> int:
        while len(self.stack) > 0 and len(self.stack[-1]) == 0:
            self.stack.pop()
        
        if len(self.stack) == 0:
            return -1
        else:
            return self.stack[-1].pop()


    def popAtStack(self, index: int) -> int:
        if index < 0 or index >= len(self.stack):
            return -1

        if len(self.stack[index]) == 0:
            return -1

        return self.stack[index].pop()

# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)
# '''