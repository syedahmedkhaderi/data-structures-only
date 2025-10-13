#   Created by Elshad Karimov on 12/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break
    
    #  Creation of Circular Doubly Linked List
    def createCDLL(self, nodeValue):
        newNode = Node(nodeValue)
        self.head = newNode
        self.tail = newNode
        newNode.prev = newNode
        newNode.next = newNode
        self.size = 1
        return "The CDLL is created successfully"


    # Insertion Method in Circular Doubly Linked List
    def insertCDLL(self, value, location):
        if self.head is None:
            return "The CDLL does not exist"
        
        newNode = Node(value)
        
        # Handle negative or out-of-bounds locations
        if location < 0:
            location = 0
        if location > self.size:
            location = self.size
            
        if location == 0:
            # Insert at beginning
            newNode.next = self.head
            newNode.prev = self.tail
            self.head.prev = newNode
            self.head = newNode
            self.tail.next = newNode
        elif location == self.size:
            # Insert at end
            newNode.next = self.head
            newNode.prev = self.tail
            self.head.prev = newNode
            self.tail.next = newNode
            self.tail = newNode
        else:
            # Insert at specific position
            tempNode = self.head
            index = 0
            while index < location - 1:
                tempNode = tempNode.next
                index += 1
            newNode.next = tempNode.next
            newNode.prev = tempNode
            newNode.next.prev = newNode
            tempNode.next = newNode
        
        self.size += 1
        return "The node has been successfully inserted"

    # Traversal of Circular Doubly Linked List
    def traversalCDLL(self):
        if self.head is None:
            print("There is not any node for traversal")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                if tempNode == self.tail:
                    break
                tempNode = tempNode.next

    # Reverse traversal of Circular Doubly Linked List
    def reverseTraversalCDLL(self):
        if self.head is None:
            print("There is not any node for reverse traversal")
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                if tempNode == self.head:
                    break
                tempNode = tempNode.prev
    
    # Search Circular Doubly Linked List
    def searchCDLL(self, nodeValue):
        if self.head is None:
            return "There is not any node in CDLL"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode  # Return the node, not just the value
                if tempNode == self.tail:
                    return None  # Return None instead of string for consistency
                tempNode = tempNode.next
    
    # Delete a node from Circular Doubly Linked List
    def deleteNode(self, location):
        if self.head is None:
            print("There is not any node to delete")
            return
        
        # Handle bounds checking
        if location < 0 or location >= self.size:
            print("Invalid location")
            return
            
        if self.size == 1:
            # Delete single node
            self.head.prev = None
            self.head.next = None
            self.head = None
            self.tail = None
            self.size = 0
            print("The node has been successfully deleted")
            return
            
        if location == 0:
            # Delete first node
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head
        elif location == self.size - 1:
            # Delete last node
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail
        else:
            # Delete middle node
            curNode = self.head
            index = 0
            while index < location - 1:
                curNode = curNode.next
                index += 1
            curNode.next = curNode.next.next
            curNode.next.prev = curNode
        
        self.size -= 1
        print("The node has been successfully deleted")
    
    # Delete entire Circular Doubly Linked List
    def deleteCDLL(self):
        if self.head is None:
            print("There is not any element to delete")
        else:
            self.tail.next = None
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
            self.size = 0
            print("The CDLL has been successfully deleted")
    


circularDLL = CircularDoublyLinkedList()
circularDLL.createCDLL(5)
circularDLL.insertCDLL(0,0)
circularDLL.insertCDLL(1,1)
circularDLL.insertCDLL(2,2)
print([node.value for node in circularDLL])
circularDLL.deleteCDLL()
print([node.value for node in circularDLL])




    
