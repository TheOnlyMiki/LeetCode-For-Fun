class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        rows, cols = range(1,m), range(1,n)

        for x in rows:
            grid[x][0] += grid[x-1][0]
        for y in cols:
            grid[0][y] += grid[0][y-1]

        top = None
        for x in rows:
            top = x-1
            for y in cols:
                
                grid[x][y] += min(grid[top][y], grid[x][y-1])

        return grid[-1][-1]
