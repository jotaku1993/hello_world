# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None:
            return None
        
        nHead = RandomListNode(0)
        pre = nHead
        p = head
        
        dct = {}
        #cnt = 1
        while p:
            node = RandomListNode(p.label)
            pre.next = node
            pre = node
            dct[p.label] = node
            p = p.next
        pre.next = None
        
        p = head
        cur = nHead.next
        while p:
            if p.random is None:
                cur.rondom = None
            else:
                value = p.random.label
                cur.random = dct[value]
            p, cur = p.next, cur.next
            
        return nHead.next
