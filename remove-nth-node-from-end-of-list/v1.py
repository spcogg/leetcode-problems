# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# works, but is slow and memory intensive
# speed: 18%
# memory: 5.6%

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # if head == [] or head ==None:
        #     return []
        current = head
        maxcount = 1  # first loop to get length
        while(current.next != None):
            maxcount += 1
            current = current.next
        current = head  # reset loop, do delete & re-point
        count = 1
        if maxcount == n:
            return head.next
        for count in range(1, maxcount):
            # print(count)
            if maxcount - (count) == n:  # difference between count and max = n from end
                current.next = current.next.next
                return head
            current = current.next
        
        return None
