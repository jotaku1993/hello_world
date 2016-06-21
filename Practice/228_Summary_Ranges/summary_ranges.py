class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        l = len(nums)
        if l == 0:
            return []
        elif l == 1:
            return [str(nums[0])]
            
        first = nums[0]
        ans = []
        for i in range(1, l):
            if nums[i] - nums[i-1] == 1:
                continue
            else:
                if first == nums[i-1]:
                    tmp = str(nums[i-1])
                else:
                    tmp = str(first) + '->' + str(nums[i-1])
                first = nums[i]
                ans.append(tmp)
        if first == nums[i]:
            tmp = str(nums[i])
        else:
            tmp = str(first) + '->' + str(nums[i])
        first = nums[i]
        ans.append(tmp)
        return ans
