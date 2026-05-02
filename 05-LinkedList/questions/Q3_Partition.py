#   Created by Elshad Karimov on 18/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

#  Question 3 - Write code to partition a linked list around a value x, 
#               such that all nodes less than x come before all nodes greater than or equal to x. 

from LinkedList import LinkedList

def partition(ll, x):
    curNode = ll.head
    ll.tail = ll.head

    while curNode:
        nextNode = curNode.next
        curNode.next = None
        if curNode.value < x:
            curNode.next = ll.head
            ll.head = curNode
        else:
            ll.tail.next = curNode
            ll.tail = curNode
        curNode = nextNode
    
    if ll.tail.next is not None:
        ll.tail.next = None

customLL = LinkedList()
customLL.generate(10,0,99)
print(customLL)
partition(customLL, 30)
print(customLL)


''' My unqiue solulu
Time Complexity: O(n)
Space Complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before = ListNode(0)   # < x
        after = ListNode(0)    # >= x

        before_curr = before
        after_curr = after

        curr = head

        while curr:
            next_node = curr.next   # Save next
            curr.next = None        # Detach node

            if curr.val < x:
                before_curr.next = curr
                before_curr = before_curr.next
            else:
                after_curr.next = curr
                after_curr = after_curr.next

            curr = next_node

        before_curr.next = after.next

        return before.next
            
'''