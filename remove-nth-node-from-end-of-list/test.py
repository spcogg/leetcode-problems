# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

"""
leetcode does some stuff in the background to translate your inputs 
# [1,2,3,4,5]
into a bunch of 'listnode' objects as per above defintion
and then sends you just the first one as the 'head' as input to this problem
"""
head = ListNode(1)  # won't work yet

print(head.val)
print(head.next)
print(head.val.next)


# testing the solution
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not isinstance(head, ListNode):
            pass  # if we had to handle incorrect input
        current = head  # assign a working pointer to the label
        
        while(current.next != None):
            print(head.next.val)
            head.val = 100
            print(head.val)
            current = head.next 
            print(current.val)
            current.val = -10
            print(current.val)
            print(current.next.val)
        
