class Solution(object)
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = [1]
        
        idx2, idx3, idx5 = 0, 0, 0
        
        for i in range(1, n):
            mini = min(ret[idx2]*2, ret[idx3]*3, ret[idx5]*5)
            ret.append(mini)
            
            while ret[idx2]*2 <= mini:
                idx2 += 1
            while ret[idx3]*3 <= mini:
                idx3 += 1
            while ret[idx5]*5 <= mini:
                idx5 += 1
        
        #print ret
        return ret[-1]
