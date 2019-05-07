# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# single pass solution to speed it up
# speed: 40ms - 93.28%
# memory: 13.3MB - 5.6%, i guess python just isn't efficient at space

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if n == 0:
            raise ValueError("can't remove 0th node from end")
        list_all = []
        current = head
        while(1):
            list_all.append(current)  # go through and get all list nodes
            if current.next == None:
                break
            current = current.next
        # now should have a list of all the nodes # print(len(list_all))
        if len(list_all) == n:  # handle removing first element first
            return head.next
        # find the element before and point to element after
        n_before = len(list_all) - n - 1
        n_remove = len(list_all) - n
        print(n_before, ' ', n_remove)
        list_all[n_before].next = list_all[n_remove].next
        return head
