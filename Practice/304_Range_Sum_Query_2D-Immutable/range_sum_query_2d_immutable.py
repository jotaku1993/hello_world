class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        m = len(matrix)
        if m == 0:
            return
        n = len(matrix[0])
        if n == 0:
            return
        self.nums = [[0] * n for x in range(m)]
        self.nums[0][0] = matrix[0][0]
        for i in range(1, m):
            self.nums[i][0] = self.nums[i-1][0] + matrix[i][0]
        for j in range(1, n):
            self.nums[0][j] = self.nums[0][j-1] + matrix[0][j]
        for i in range(1, m):
            for j in range(1, n):
                self.nums[i][j] = matrix[i][j] + self.nums[i-1][j] + self.nums[i][j-1] - self.nums[i-1][j-1]
                
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if row1 == 0 and col1 == 0:
            return self.nums[row2][col2]
        if row1 == 0:
            return self.nums[row2][col2] - self.nums[row2][col1-1]
        if col1 == 0:
            return self.nums[row2][col2] - self.nums[row1-1][col2]
        return self.nums[row2][col2] - self.nums[row1-1][col2] - self.nums[row2][col1-1] + self.nums[row1-1][col1-1]


# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)
