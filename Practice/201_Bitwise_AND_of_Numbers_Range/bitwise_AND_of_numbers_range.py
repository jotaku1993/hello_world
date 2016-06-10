class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == n:
            return m
        
        move = 0
        while m != n:
            m >>= 1
            n >>= 1
            move += 1
        return m << move
