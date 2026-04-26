#Doubly linked lists are just normal, singly linked lists with one added feature,
#a link to the previous node as well in addition to a link to the next node.
#Although the worst case time complexities of all operations in a doubly linked list are same as that of a singly linked list,
#Some operations are technically faster. For example, lookup or searching, is O(n/2) as search can begin from both ends
#But O(n/2) = O(n), so it is still the same as that for a singly linked list.

#Implementation of doubly linked list is almost exactly the same as that for singly linked list,
#With just the added feature of the pointer to the previous node.
#We'll have the same methods which do the exact same thing. The pars which will be different from the singly linked list are explained
#So lets implement it.

class Node:
    def __init__(self, value):
        # Represents a node in the DLL with value and next/prev pointers
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        # Initialize an empty DLL with head/tail and size tracking
        self.head = None
        self.tail = None
        self.prev = None
        self.length = 0

    def append(self, value):
        # Add a node to the end; update tail and link prev/next pointers
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head

        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        # Add a node to the beginning; update head and link pointers
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def insert(self, index, value):
        # Insert at index; prepends/appends when out of range boundaries
        new_node = Node(value)

        if index <= 0:
            self.prepend(value)
            return

        if index >= self.length:
            self.append(value)
            return
        #   Method 3
        else:
            leader = self.traversetoindex(index - 1)
            holder = leader.next
            leader.next = new_node
            new_node.next = holder
            new_node.prev = leader
            holder.prev = new_node
            self.length += 1

        ''' - Method 1
        while i <= self.length:
            if i == index - 1:
                new_node.next, temp.next = temp.next, new_node
                self.length += 1
                break # To break the while loop and exit.
            temp = temp.next
            i += 1
        '''
        '''
        # Method 2
        while i < index - 1:
            temp = temp.next
            i += 1

        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        '''

    def traversetoindex(self, index):
        # Return node at index by walking from head
        curr_node = self.head
        i = 0
        while i != index:
            curr_node = curr_node.next
            i += 1
        return curr_node

    def delete(self, index):
        # Delete node at index; updates head/tail and relinks neighbors
        temp = self.head
        i = 0
        if index < 0 or index >= self.length:
            print("Entered wrong index")
            return

        if index == 0:
            self.head = self.head.next
            self.length -= 1
            if self.length == 0:
                self.tail = None  # Handle empty list
            else:
                self.head.prev = None
            return

        if index == self.length - 1:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return

        # Method 3
        leader = self.traversetoindex(index - 1)
        unwanted_node = leader.next
        holder = unwanted_node.next
        leader.next = holder
        holder.prev = leader
        self.length -= 1

        ''' Method 1
        while i <= self.length:
            if i == index - 1:
                temp.next = temp.next.next
                self.length -= 1
                break
            i += 1
            temp = temp.next
        '''
        ''' Method 2
        while i < index - 1:
            temp = temp.next
            i += 1
        temp.next = temp.next.next
        if index == self.length - 1:
            self.tail = temp  # Update tail if last node was deleted
        self.length -= 1
        '''

    def search(self, target):
        # Linear search for value; returns index or -1 if not found
        current_node = self.head
        index = 0
        while current_node:
            if current_node.value == target:
                return index
            current_node = current_node.next
            index += 1
        return -1

    def set_value(self, index, value):
        # Set a node's value at index; returns True if successful
        node = self.traversetoindex(index) if 0 <= index < self.length else None
        if node:
            node.value = value
            return True
        return False

    def clear_DLL(self):
        # Remove all nodes and reset the list
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        if index < self.length // 2:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
        else:
            current_node = self.tail
            for _ in range(self.length - 1, index, -1):
                current_node = current_node.prev
        return current_node

    def printl(self):
        # Return a list-like string of values with the current length
        arr = []
        temp = self.head
        while temp is not None:
            arr.append(temp.value)
            temp = temp.next
        return f"{arr} | Length = {str(self.length)}"

    
    def __str__(self) -> str:
        temp_node = self.head
        result = ""
        while temp_node:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += "<->"
            temp_node = temp_node.next
        return result



d = DoublyLinkedList()
d.append(10)
d.append(5)
d.append(6)
d.prepend(1)
d.insert(2,22)
d.delete(3)
print(d.printl())