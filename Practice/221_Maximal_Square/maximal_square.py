class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        if n == 0:
            return 0
            
        ans = [[0]*n for x in range(m)]
        ret = 0
        
        for i in range(n):
            if matrix[0][i] == '1':
                ans[0][i] = 1
                ret = 1
                
        for i in range(m):
            if matrix[i][0] == '1':
                ans[i][0] = 1
                ret = 1
                
        #print ans
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    if ans[i-1][j-1] > 0 and ans[i-1][j] > 0 and ans[i][j-1] > 0:
                        ans[i][j] = min(ans[i][j-1], ans[i-1][j], ans[i-1][j-1]) + 1
                        if ans[i][j] > ret:
                            ret = ans[i][j]
                    else:
                        ans[i][j] = 1
        #print ans
        return ret*ret
