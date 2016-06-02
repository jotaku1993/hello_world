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
            if nums[i] not in dct:
                dct[nums[i]] = 1
            else:
                del dct[nums[i]]
        return dct.items()[0][0]
