class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        if l == 0:
            return []
        elif l == 1:
            return [nums[0]]
            
        maj1, maj2 = nums[0], None
        cnt1, cnt2 = 1, 0
        for i in range(1, l):
            if nums[i] == maj1:
                cnt1 += 1
            elif nums[i] == maj2:
                cnt2 += 1
            elif cnt1 == 0:
                maj1 = nums[i]
                cnt1 = 1
            elif cnt2 == 0:
                maj2 = nums[i]
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1
                
        cnt1, cnt2 = 0, 0
        for i in range(l):
            if nums[i] == maj1:
                cnt1 += 1
            elif nums[i] == maj2:
                cnt2 += 1
        ans = []
        if cnt1 > l // 3:
            ans.append(maj1)
        if cnt2 > l // 3:
            ans.append(maj2)
        return ans
