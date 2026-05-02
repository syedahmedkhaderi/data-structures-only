#   Created by Elshad Karimov on 19/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

# Question 5 - Intersection

from LinkedList import LinkedList, Node

def intersection(llA, llB):
    if llA.tail is not llB.tail:
        return False
    
    lenA = len(llA)
    lenB = len(llB)

    shorter = llA if lenA < lenB else llB
    longer = llB if lenA < lenB else llA

    diff = len(longer) - len(shorter)
    longerNode = longer.head
    shorterNode = shorter.head

    for i in range(diff):
        longerNode = longerNode.next
    
    while shorterNode is not longerNode:
        shorterNode = shorterNode.next
        longerNode = longerNode.next
    
    return longerNode


# Helper addition method
def addSameNode(llA, llB, value):
    tempNode = Node(value)
    llA.tail.next = tempNode
    llA.tail = tempNode
    llB.tail.next = tempNode
    llB.tail = tempNode

llA = LinkedList()
llA.generate(3,0, 10)

llB = LinkedList()
llB.generate(4,0, 10)

addSameNode(llA, llB, 11)
addSameNode(llA, llB, 14)

print(llA)
print(llB)

print(intersection(llA, llB))



''' Hashtable approach

Time Complexity: O(n + m) ; n = len(A), m = len(B)
Space Complexity: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen = set()

        curr1 = headA
        while curr1:
            seen.add(curr1)
            curr1 = curr1.next
        
        curr2 = headB
        while curr2:
            if curr2 in seen:
                return curr2
            curr2 = curr2.next

        return None
'''

''' Longer list approach
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def get_length(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length
        
        # Get the lengths of both ll
        len_a = get_length(headA)
        len_b = get_length(headB)

        a, b = headA, headB

        # Move longer list forward
        if len_a > len_b:
            for _ in range(len_a - len_b):
                a = a.next
        else:
            for _ in range(len_b - len_a):
                b = b.next

        # now traverse both lists comparing the elements.
        while a or b:
            if a == b:
                return a
            a = a.next
            b = b.next

        return None

'''