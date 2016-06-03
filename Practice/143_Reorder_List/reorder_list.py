# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        #print slow.val, fast==None
        
        #find the middle point, note it start.
        if fast == None:
            start = slow
        else:
            start = slow.next
        
        #Then reverse the linked list from start
        p = start
        pre = None
        while p:
            tmp = p.next
            p.next = pre
            pre = p
            p = tmp
            
        #pre is the new start
        p1, p2 = head, pre
        while p2:
            tmp1 = p1.next
            tmp2 = p2.next
            p1.next = p2
            p2.next = tmp1
            p1 = tmp1
            p2 = tmp2
        if p1 is not None:
            p1.next = None
        
        return
