# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.path1 = None
        self.path2 = None
        self.flag = 0
        self.dfs(root, [root], [root], p, q)
        
        l1 = len(self.path1)
        l2 = len(self.path2)
        
        ans = root
        #print l1, l2
        for i in range(min(l1, l2)):
            if self.path1[i] == self.path2[i]:
                ans = self.path1[i]
            else:
                break
            
        return ans
        
    def dfs(self, root, p1, p2, p, q):
        if self.flag == 2:
            return
        if root is None:
            return
        #print root.val
        if root == p:
            self.path1 = p1[:]
            self.flag += 1
        if root == q:
            self.path2 = p2[:]
            self.flag += 1
            
        p1.append(root.left)
        p2.append(root.left)
        self.dfs(root.left, p1, p2, p, q)
        p1.pop()
        p2.pop()
        
        p1.append(root.right)
        p2.append(root.right)
        self.dfs(root.right, p1, p2, p, q)
        p1.pop()
        p2.pop()
