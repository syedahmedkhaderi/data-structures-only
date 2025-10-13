import sys

class MaxHeap:

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.heap = [0] * (self.maxsize + 1)
        self.heap[0] = sys.maxsize
        self.front = 1
# The sys.maxsize is the largest possible integer in Python.
# it is used to initialize the first element of the heap with a value that is greater than any possible element in the heap.
# This is done to ensure that the first element of the heap is always greater than any possible element in the heap.
# We are starting the heap with index 1, so we need to add 1 to the maxsize.


# Because of the 1-indexing the formula for the parents and children becomes simpler
    def parent(self, pos):
        return pos//2 
        # // is floor division, it returns the integer part of the division.
        # pos//2 is the parent of the current position.

    def leftChild(self, pos):
        return 2 * pos
        # 2 * pos is the left child of the current position.

    def rightChild(self, pos):
        return 2 * pos + 1
        # 2 * pos + 1 is the right child of the current position.

#Method that returns true if the passed node is a leaf node.
#All the nodes in the second half of the heap(when viewed as an array) are leaf nodes.
#So we just check if the position entered is >= half of the size of the heap and <= size of the heap.
    def isLeaf(self, pos):
        return pos * 2 > self.size
        # pos * 2 > self.size is the condition to check if the current position is a leaf node.

    def swap(self, fpos, spos):
        self.heap[fpos], self.heap[spos] = self.heap[spos], self.heap[fpos]
        # swap the two elements in the heap. Using tuple unpacking.
        
#Method to heapify the node at pos.
#This method will be called whenever the heap property is disturbed, to restore the heap property of the heap
#We will check if the concerned node is a leaf node or not first. If it is, then no need to do anything.
#If it is not and it is smaller than any of its children, then we will check which of its children is largest
#and swap the node with its largest child. After doing this, the heap property may be disturbed. 
#So we will call max_heapify again.
    def maxHeapify(self, pos):
        #If the node is a non-leaf node and smaller than any of its child
        if not self.isLeaf(pos):
            if self.heap[pos] < self.heap[self.leftChild(pos)] or self.heap[pos] < self.heap[self.rightChild(pos)]:

                #Swap with the left child and heapify the left child
                if self.heap[self.leftChild(pos)] > self.heap[self.rightChild(pos)]:
                    self.swap(pos, self.leftChild(pos))
                    self.maxHeapify(self.leftChild(pos))
                
                #Swap with the right child and heapify the right child
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.maxHeapify(self.rightChild(pos))

#Method to insert a node into the heap . First we will increase the size of the heap by 1.
#Then we will insert the element to end of the heap. Now this new element may violate the heap property.
#So we will keep checking its value with its parent's value.
#And keep swapping it with its parent as long as the parent is smaller than the element.
    def insert(self, element):
        # To make sure it doesn't exceed the maximum size of heap allotted.
        if self.size >= self.maxsize:
            return

        self.size += 1
        self.heap[self.size] = element
        curr = self.size
        while self.heap[curr] > self.heap[self.parent(curr)]:
            self.swap(curr, self.parent(curr))
            curr = self.parent(curr)
    
#Method to remove and return the maximum element from the heap . The maximum element will be at the root.
#So we will copy the element at the end of the heap into the root node
#and delete the last node, which will leave the heap property disturbed
#So we will finally call heapify on the root node to restore the heap property
    def extract_max(self):
        pop = self.heap[self.front]
        self.heap[self.front] = self.heap[self.size]
        self.size -= 1
        self.maxHeapify(self.front)
        return pop
    
    def print_heap(self):
        for i in range(1, (self.size//2) + 1):
            print("Parent: " + str(self.heap[i]) + " Left Child: " + str(self.heap[2 * i]) + " Right Child: " + str(self.heap[2 * i + 1]))


my_heap = MaxHeap(15)
my_heap.insert(5)
my_heap.insert(3)
my_heap.insert(17)
my_heap.insert(10)
my_heap.insert(84)
my_heap.insert(19)
my_heap.insert(6)
my_heap.insert(22)
my_heap.insert(9)
print("--------------------------------")
my_heap.print_heap()
print("--------------------------------")
print("The Max val is " + str(my_heap.extract_max()))
print("--------------------------------")
my_heap.insert(100)
my_heap.print_heap()
print("--------------------------------")
print("The Max val is " + str(my_heap.extract_max()))
print("--------------------------------")
