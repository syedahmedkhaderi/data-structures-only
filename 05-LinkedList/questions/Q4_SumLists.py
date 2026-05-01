#   Created by Elshad Karimov on 18/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

# Question 4 - Sum Lists

from LinkedList import LinkedList

def sumList(llA, llB):
    n1 = llA.head
    n2 = llB.head
    carry = 0
    ll = LinkedList()

    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next
        ll.add(int(result % 10))
        carry = result // 10
    
    return ll

llA = LinkedList()
llA.add(7)
llA.add(1)
llA.add(6)


llB = LinkedList()
llB.add(5)
llB.add(9)
llB.add(2)
print(llA)
print(llB)
print(sumList(llA, llB))



''' My unique solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = l1, l2
        num1 = num2 = ''

        while curr1:
            num1 += str(curr1.val)
            curr1 = curr1.next
        while curr2:
            num2 += str(curr2.val)
            curr2 = curr2.next

        num3 = str(int(num1[::-1]) + int(num2[::-1]))

        dummy = ListNode(0)
        curr = dummy
        for i in num3[::-1]:
            curr.next = ListNode(int(i)) # 0(dummy) --> i --> ....
            curr = curr.next

        return dummy.next
        
         
         
'''

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = l1, l2

        dummy = ListNode(0)
        curr = dummy

        carry = 0

        while n1 or n2 or carry:
            res = carry
            if n1:
                res += n1.val
                n1 = n1.next
            if n2:
                res += n2.val
                n2 = n2.next
            
            curr.next = ListNode(res % 10)
            carry = res // 10

            curr = curr.next

        return dummy.next
'''