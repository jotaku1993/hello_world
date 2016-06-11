class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 0:
            return 0
        if sum(nums) < s:
            return 0
            
        fast, slow = 0, 0
        suma = 0
        ret = 1<<32
        
        while fast < l:
            while fast < l and suma < s:
                suma += nums[fast]
                fast += 1
                
            while slow < l and suma >= s:
                ret = min(ret, fast-slow)
                suma -= nums[slow]
                slow += 1
            
            
            
        return ret
            
