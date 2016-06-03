class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        l = len(s)
        if l == 0:
            return False
        
        ans = [False] * l
        
        for i in range(l):
            if s[0:i+1] in wordDict:
                ans[i] = True
            for j in range(i):
                if ans[j] is True and s[j+1:i+1] in wordDict:
                    ans[i] = True
        print ans
        return ans[-1]
