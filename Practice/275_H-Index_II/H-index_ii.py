class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        l = len(citations)
        if l == 0:
            return 0
        left, right = 0, l-1
        while left <= right:
            mid = (left + right) // 2
            if l - mid < citations[mid]:
                right = mid - 1
            elif l - mid > citations[mid]:
                left = mid + 1
            else:
                return l - mid
                
        return l - left
