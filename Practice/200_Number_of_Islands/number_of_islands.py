class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        
        ret = 0
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0 ,0]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '+' or grid[i][j] == '0':
                    continue
                
                grid[i][j] = '+'
                ret += 1
                q = []
                q.append([i, j])
                while len(q) > 0:
                    ti, tj = q.pop(0)
                    for k in range(4):
                        ni, nj = ti + dx[k], tj + dy[k]
                        if (0 <= ni and ni < m) and (0 <= nj and nj < n) and grid[ni][nj] == '1':
                            q.append([ni, nj])
                            grid[ni][nj] = '+'
        #print grid
        return ret
