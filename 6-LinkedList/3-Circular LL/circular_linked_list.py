class Node:
    def __init__(self, value):
        # Node for circular linked list with data and next pointer
        self.data = value
        self.next = None


class CircularLinkedList:
    def __init__(self):
        # Initialize empty circular linked list with head, tail, and size tracking
        self.head = None
        self.tail = None
        self.size = 0


    def is_empty(self):
        # Check if the circular list is empty
        return self.size == 0

    def prepend(self, value):
        # Add node to the beginning; update head and maintain circular link
        new_node = Node(value)
        if self.is_empty():
            new_node.next = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.tail.next = new_node
        self.head = new_node
        self.size += 1


    def append(self, value):
        # Add node to the end; update tail and maintain circular link
        new_node = Node(value)
        if self.is_empty():
            new_node.next = new_node
            self.head = new_node
        else:
            new_node.next = self.head
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1


    def insert(self, value, index):
        # Insert node at specific index; handle boundary cases
        if index <= 0:
            self.prepend(value)
            return
        if index >= self.size:
            self.append(value)
            return
        
        new_node = Node(value)
        temp = self.head
        for i in range(index - 1):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
        self.size += 1
    
    def get(self, index):
        # Get node at index; return None for invalid indices
        if index == -1:
            return self.tail
        elif index < -1 or index >= self.size:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current
    
    def search(self, target):
        # Search for target value; return True if found, False otherwise
        if self.is_empty():
            return False
        current = self.head
        while True:
            if current.data == target:
                return True
            current = current.next
            if current == self.head:  # Stop condition for circular list
                break
        return False

    def update(self, index, value):
        # Update node value at index; return True if successful
        temp = self.get(index)
        if temp:
            temp.data = value
            return True
        return False


    def remove_first(self):
        # Remove and return first node; handle empty list case
        if self.is_empty():
            print("The list is empty")
            return None
        old_head = self.head
        self.tail.next = old_head.next
        self.head = old_head.next
        self.size -= 1
        if self.is_empty():
            self.tail = None
        return old_head.data


    def remove_last(self):
        # Remove and return last node; handle empty list case
        if self.is_empty():
            print("The list is empty")
            return None
        if self.size == 1:
            value = self.head.data
            self.head = self.tail = None
            self.size = 0
            return value
        
        temp = self.head
        for i in range(self.size - 2):
            temp = temp.next
        value = temp.next.data
        self.tail = temp
        self.tail.next = self.head
        self.size -= 1
        return value


    def remove(self, index):
        # Remove node at index; handle boundary cases
        if self.is_empty() or index < 0 or index >= self.size:
            print("List is empty or the index is invalid")
            return None
        if index == 0:
            return self.remove_first()
        if index == self.size - 1:
            return self.remove_last()
        
        temp = self.head
        for i in range(index - 1):
            temp = temp.next
        value = temp.next.data
        temp.next = temp.next.next
        self.size -= 1
        return value


    def print_list(self):
        # Print all nodes in the circular list
        if self.is_empty():
            print("List is empty")
            return
        temp = self.head
        for i in range(self.size):
            print(temp.data, end='-->')
            temp = temp.next
        print()
    
    def __str__(self):
        # String representation of the circular list
        if self.is_empty():
            return "Empty circular list"
        temp_node = self.head
        result = ''
        for i in range(self.size):
            result += str(temp_node.data)
            if i < self.size - 1:
                result += ' -> '
            temp_node = temp_node.next
        return result
    
    def clear_cll(self):
        # Clear all nodes and reset the circular list
        if self.size == 0:
            return  # If the list is empty, just return
        self.tail.next = None  # Breaking the circular link
        self.head = None
        self.tail = None
        self.length = 0


# Test the circular linked list
circ_list = CircularLinkedList()
circ_list.add_first(1)
circ_list.add_last(2)
circ_list.add_last(3)
circ_list.add_last(5)
circ_list.add_particular(4, 4)
circ_list.print_list()
print(circ_list.remove_first())
circ_list.print_list()
print(circ_list.remove_last())
circ_list.print_list()
print(circ_list.remove_particular(2))
circ_list.print_list()