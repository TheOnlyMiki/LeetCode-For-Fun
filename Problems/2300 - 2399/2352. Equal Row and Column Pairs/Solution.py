class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Option 2 - HashTable store the row, and read col if match row
        rows = {}
        for row in grid:
            row = tuple(row)
            if row in rows:
                rows[row] += 1
            else:
                rows[row] = 1

        n = len(grid[0])
        cols = range(n)
        output = 0
        for i in range(len(grid)):
            col = [0] * n
            for j in cols:
                col[j] = grid[j][i]

            if tuple(col) in rows:
                output += rows[tuple(col)]

        return output

        # Option 1 - BF method, too slowly
        """
        output = 0
        cols = range(len(grid[0]))

        for i in range(len(grid)):
            for j in cols:
                temp = True
                for k in cols:
                    if grid[i][k] != grid[k][j]:
                        temp = False
                        break

                if temp:
                    output += 1

        return output
        """
