class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        l = len(nums)
        if l == 0:
            return ''
        elif l == 1:
            return str(nums[0])
            
        fzero = 0
        for i in range(l):
            if nums[i] != 0:
                fzero = 1
                break
        if fzero == 0:
            return '0'
        num = self.sort(nums)
        #print num
        return ''.join(map(str,num[::-1]))
        
    def sort(self, nums):
        l = len(nums)
        for i in range(l):
            for j in range(i+1, l):
                if self.cmp(nums[i], nums[j]) == 1:
                    nums[i], nums[j] = nums[j], nums[i]
        return nums
                    
                
    
    #if n1 larger, return 1; same, return 0; n2 larger, return -1
    def cmp(self, n1, n2):
        if n1 == n2:
            return 0
        s1 = str(n1)
        s2 = str(n2)
        
        if s1 + s2 > s2 + s1:
            return 1
        else:
            return -1
