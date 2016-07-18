class FenwickTree(object):
    def __init__(self, n):
        self.sum_array = [0] * (n + 1)
        self.n = n
 
    def lowbit(self, x):
        return x & -x
 
    def add(self, x, val):
        while x <= self.n:
            self.sum_array[x] += val
            x += self.lowbit(x)
 
    def sum(self, x):
        res = 0
        while x > 0:
            res += self.sum_array[x]
            x -= self.lowbit(x)
        return res
        
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        l = len(nums)
        if l == 0:
            return
        self.nums = nums
        self.fTree = FenwickTree(l)
        for i in range(1, l+1):
            self.fTree.add(i, nums[i-1])
        

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        self.fTree.add(i+1, val - self.nums[i])
        self.nums[i] = val
        return
        

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.fTree.sum(j+1) - self.fTree.sum(i)
        


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)
