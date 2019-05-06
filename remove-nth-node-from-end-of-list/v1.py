# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # add in checker for null list
        current = head
        maxcount = 1  # first loop to get length
        while(current.next != None):
            maxcount += 1
            current = current.next
        current = head  # reset loop, do delete & re-point
        count = 1
        if maxcount == n:
            return head.next
        while(current.next != None):
            if maxcount - count == n:
                #print('current:', current.val)
                current.next = current.next.next
                # print('next:', current.next.val)
                break
                # do checks on where it is in the cont
                # and update the pointers accordingly
            current = current.next        
            count += 1
        return head
                    
                    