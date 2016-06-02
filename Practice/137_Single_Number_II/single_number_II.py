class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 1:
            return nums[0]
            
        dct = {}
        
        for i in range(l):
            if nums[i] in dct:
                if dct[nums[i]] == 1:
                    dct[nums[i]] = 2
                else:
                    del dct[nums[i]]
            else:
                dct[nums[i]] = 1
                
        return dct.items()[0][0]
