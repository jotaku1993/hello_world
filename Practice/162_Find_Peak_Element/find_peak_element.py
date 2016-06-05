class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 1:
            return 0
        return self.bs(nums, 0, l-1)
        
    def bs(self, nums, left, right):
        mid = (left + right) // 2
        if (left == mid or nums[mid-1] < nums[mid]) and (right == mid or nums[mid+1] < nums[mid]):
            return mid
        elif nums[mid] < nums[mid+1]:
            return self.bs(nums, mid+1, right)
        else:
            return self.bs(nums, left, mid-1)
