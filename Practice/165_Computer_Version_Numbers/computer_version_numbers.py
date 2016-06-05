class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        s1 = version1.split('.')
        s2 = version2.split('.')
        
        l1 = len(s1)
        l2 = len(s2)
        
        if l1 > l2:
            for i in range(l1-l2):
                s2.append('0')
        elif l1 < l2:
            for i in range(l2-l1):
                s1.append('0')
        
        for i in range(max(l1,l2)):
            if int(s1[i]) < int(s2[i]):
                return -1
            elif int(s1[i]) > int(s2[i]):
                return 1
            else:
                pass
        return 0
        
