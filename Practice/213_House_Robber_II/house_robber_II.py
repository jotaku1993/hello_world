class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 0:
            return 0
        elif l == 1:
            return nums[0]
            
            
        best0, best1 = 0, 0
        best2, best3 = 0, 0
        for i in range(l-1):
            tmp1, tmp2 = best0, best2
            best0 = max(best0, best1)
            best2 = max(best2, best3)
            best1, best3 = tmp1 + nums[i], tmp2 + nums[i+1]
            
        return max(best0, best1, best2, best3)
