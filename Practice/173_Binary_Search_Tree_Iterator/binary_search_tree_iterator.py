# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stk = []
        while root:
            self.stk.append(root)
            root = root.left
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.stk) != 0:
            return True
        else:
            return False
        

    def next(self):
        """
        :rtype: int
        """
        ret = self.stk.pop()
        #the following smallest will in the right child tree
        right = ret.right
        while right:
            self.stk.append(right)
            right = right.left
        return ret.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
