class Solution(object):
    #Revise the array in place, better
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
        
        #tmp = [[0] * n for i in range(m)]
        #some notations
        d2d = 0
        l2l = 1
        l2d = 2
        d2l = 3
        
        dx = [0, 0, -1, 1, 1, 1, -1, -1]
        dy = [-1, 1, 0, 0, 1, -1, -1, 1]
        
        for i in range(m):
            for j in range(n):
                cnt = 0
                for k in range(8):
                    x, y = i + dx[k], j + dy[k]
                    if (x >= 0 and x < m) and (y >= 0 and y < n):
                        if board[x][y] == 1 or board[x][y] == 2:
                            cnt += 1
                #print cnt
                if cnt >= 2 and cnt < 3:
                    pass
                elif cnt == 3:
                    if board[i][j] == 0:
                        board[i][j] = 3
                else:
                    if board[i][j] == 1:
                        board[i][j] = 2
        #print tmp
        for i in range(m):
            for j in range(n):
                board[i][j] %= 2
        return
