class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if k >= 10 or n < 1:
            return []
            
        self.ans = []
        
        self.bkt([], 0, k, n)
        return self.ans
        
    def bkt(self, tmp, level, k, n):
        if level == k and sum(tmp) == n:
            self.ans.append(tmp[:])
            return
        if level >= k:
            return
        
        for i in range(1, 10):
            if len(tmp) > 0 and i <= tmp[-1]:
                continue
            tmp.append(i)
            #print tmp
            if sum(tmp) > n:
                tmp.pop()
                continue
            self.bkt(tmp, level+1, k, n)
            tmp.pop()
