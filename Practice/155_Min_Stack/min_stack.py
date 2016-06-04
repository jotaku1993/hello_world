class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk = []
        self.mstk = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stk.append(x)
        if len(self.mstk) == 0 or x <= self.mstk[-1]:
            self.mstk.append(x)
        

    def pop(self):
        """
        :rtype: void
        """
        if (self.stk[-1] == self.mstk[-1]):
            self.mstk.pop()
        self.stk.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stk[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.mstk[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
