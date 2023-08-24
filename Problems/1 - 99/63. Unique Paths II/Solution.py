class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # Option 2
        n = len(obstacleGrid[0])

        grid = [ [0]*n for _ in obstacleGrid ]

        cols = range(n)

        grid[0][0] = 1 if obstacleGrid[0][0] == 0 else 0

        top = None
        for x in range(len(obstacleGrid)):
            top = x-1
            for y in cols:
                if obstacleGrid[x][y] == 0:
                    grid[x][y] += grid[top][y] if x > 0 else 0
                    grid[x][y] += grid[x][y-1] if y > 0 else 0

        return grid[-1][-1]

        # Option 1
        if obstacleGrid[0][0] == 1:
            return 0
            
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        grid = [ [0]*n for _ in obstacleGrid ]
        rows, cols = range(1, m), range(1, n)
        grid[0][0] = 1

        for x in rows:
            if obstacleGrid[x][0] == 1:
                break
            grid[x][0] = 1

        for y in cols:
            if obstacleGrid[0][y] == 1:
                break
            grid[0][y] = 1

        top = None
        for x in rows:
            top = x-1
            for y in cols:
                if obstacleGrid[x][y] == 0:
                    grid[x][y] = grid[top][y] + grid[x][y-1]

        return grid[-1][-1]
