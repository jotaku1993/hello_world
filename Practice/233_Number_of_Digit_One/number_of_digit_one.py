class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        ans = 0
        m = 1
        while m <= n:
            a = n // m
            b = n % m
            ans = ans + (8 + a) // 10 * m
            if (a % 10 == 1):
                ans += b + 1
            m = m * 10
            
        return ans
