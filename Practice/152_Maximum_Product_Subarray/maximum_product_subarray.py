class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 0:
            return 0
        elif l == 1:
            return nums[0]
            
        maxi = nums[0]
        mini = nums[0]
        #initialize it with first element
        ans = maxi
        #start from the second element
        for i in range(1, l):
            #calculate the new product first
            tmp1, tmp2 = maxi*nums[i], mini*nums[i]
            #then compare them
            maxi = max(nums[i], max(tmp1, tmp2))
            mini = min(nums[i], min(tmp1, tmp2))
            #update the maximum
            ans = max(ans, maxi)
        return ans
