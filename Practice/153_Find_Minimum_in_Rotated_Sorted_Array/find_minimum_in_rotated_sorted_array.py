class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 1:
            return nums[0]
        
        left, right = 0, l-1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[left] <= nums[mid] and nums[mid] <= nums[right]:
               return nums[left]
            elif nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid
