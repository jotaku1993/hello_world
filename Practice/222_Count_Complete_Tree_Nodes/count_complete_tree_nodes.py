# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
            
        l = self.getLeft(root)
        r = self.getRight(root)
        #print l, r, root.val
        if l == r:
            return (2<<l) - 1
        else:
            return self.countNodes(root.left) + self.countNodes(root.right) + 1
            
    def getLeft(self, root):
        p = root
        cnt = 0
        while p.left is not None:
            p = p.left
            cnt += 1
        return cnt
        
    def getRight(self, root):
        p = root
        cnt = 0
        while p.right is not None:
            p = p.right
            cnt += 1
        return cnt
