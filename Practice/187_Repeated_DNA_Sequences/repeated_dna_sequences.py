class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dct = {}
        ans = []
        l = len(s)
        if l < 10:
            return ans
        
        for i in range(l-9):
            if s[i:i+10] in dct:
                if s[i:i+10] in ans:
                    pass
                else:
                    ans.append(s[i:i+10])
            else:
                dct[s[i:i+10]] = None
        return ans
