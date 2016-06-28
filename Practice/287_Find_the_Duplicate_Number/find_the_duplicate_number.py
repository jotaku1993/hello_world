class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fast, slow = 0, 0
        slow = nums[slow]
        fast = nums[nums[fast]]
        while fast != slow:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
        #print fast, slow
        ans = 0
        while slow != ans:
            slow = nums[slow]
            ans = nums[ans]
            
        return ans
