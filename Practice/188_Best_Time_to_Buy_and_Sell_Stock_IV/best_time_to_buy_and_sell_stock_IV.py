class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        l = len(prices)
        if k == 0 or l < 2:
            return 0
        #if k is large, we can make a deal every day
        if k > l // 2:
            ret = 0
            for i in range(1, l):
                if prices[i] - prices[i-1] > 0:
                    ret += prices[i] - prices[i-1]
            return ret
        
        #if k is small, initialize the sell and buy list
        hold = [-1<<32] * k
        release = [0] * k
        
        #for every day, make a decision if buy or sell the stock
        for i in range(l):
            for j in range(k-1, -1, -1):
                release[j] = max(release[j], hold[j]+prices[i])
                if j == 0:
                    hold[j] = max(hold[j], -prices[i])
                else:
                    hold[j] = max(hold[j], release[j-1]-prices[i])

        return release[-1]
