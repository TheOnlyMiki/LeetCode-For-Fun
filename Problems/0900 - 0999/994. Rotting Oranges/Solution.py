class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row, col = len(grid), len(grid[0])
        fresh = 0
        step = 0
        cols = range(col)
        moves = [(0,1), (1,0), (0,-1), (-1,0)]
        record = []
        
        for i in range(row):
            for j in cols:
                if grid[i][j] == 2:
                    record.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1

        while record and fresh != 0:
            temp = []
            for x, y in record:
                for new_x, new_y in moves:
                    new_x, new_y = x + new_x, y + new_y
                    if -1 < new_x < row and -1 < new_y < col and grid[new_x][new_y] == 1:
                        grid[new_x][new_y] = 2
                        temp.append((new_x, new_y))

            fresh -= len(temp)
            step += 1
            record = temp
        
        return step if fresh == 0 else -1
