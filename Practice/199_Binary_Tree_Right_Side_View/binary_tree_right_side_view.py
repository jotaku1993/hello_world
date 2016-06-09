# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        
        self.lst = []
        
        self.dfs(root, 0)
        #print self.lst
        ans = []
        for i in range(len(self.lst)):
            ans.append(self.lst[i][-1])
        return ans
        
    def dfs(self, root, level):
        if root is None:
            return
        #print root.val
        if len(self.lst) <= level:
            self.lst.append([])
        
        self.lst[level].append(root.val)
        self.dfs(root.left, level+1)
        self.dfs(root.right, level+1)
        
