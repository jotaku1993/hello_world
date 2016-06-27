class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        ans = 0
        for i in range(1, l+1):
            ans ^= i
            
        for i in range(l):
            ans ^= nums[i]
            
        return ans
