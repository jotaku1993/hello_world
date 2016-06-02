class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        l = len(s)
        if l <= 1:
            return [[s]]
            
        self.ans = []
        self.add(s, 0, [], l)
        return self.ans
        
    def add(self, s, poi, tmp, l):
        #print tmp, poi
        if poi == l:
            self.ans.append(tmp[:])
            return
        for i in range(1, l+1-poi):
            test = s[poi:poi+i]
            if test == test[::-1]:
                tmp.append(test)
                self.add(s, poi+i, tmp, l)
                tmp.pop()
            else:
                continue
            
