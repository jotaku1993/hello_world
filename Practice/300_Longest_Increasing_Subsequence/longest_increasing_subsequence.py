class Solution(object):
    #runtime O(n^2), not the best one
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l <= 1:
            return l
        ans = [1] * l
        ret = 0
        for i in range(1, l):
            tempMax = 1
            for j in range(0, i):
                if (nums[i] > nums[j]) and (ans[j] + 1 > tempMax):
                    tempMax = ans[j] + 1
                #print tempMax
            ans[i] = tempMax
            #print ans
            if tempMax > ret:
                ret = tempMax
        return ret
