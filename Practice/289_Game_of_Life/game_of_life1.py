class Solution(object):
    #Using extra space, not a good solution.
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m == 0:
            return
        n = len(board[0])
        if n == 0:
            return
        
        tmp = [[0] * n for i in range(m)]
        
        dx = [0, 0, -1, 1, 1, 1, -1, -1]
        dy = [-1, 1, 0, 0, 1, -1, -1, 1]
        
        for i in range(m):
            for j in range(n):
                cnt = 0
                for k in range(8):
                    x, y = i + dx[k], j + dy[k]
                    if (x >= 0 and x < m) and (y >= 0 and y < n) and board[x][y] == 1:
                        cnt += 1
                #print cnt
                if cnt >= 2 and cnt < 3:
                    tmp[i][j] = board[i][j]
                elif cnt == 3:
                    tmp[i][j] = 1
                else:
                    pass
        #print tmp
        for i in range(m):
            for j in range(n):
                board[i][j] = tmp[i][j]
        return
