# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return None
        fast, slow = head, head
        
        meet = None
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break
            
        if fast is None or fast.next is None:
            return None
        
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return fast
