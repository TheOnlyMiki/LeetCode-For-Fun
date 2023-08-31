class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        col_0 = False
        row_0 = False

        # Option 2 - Space O(1)
        for x in range(m):
             if matrix[x][0] == 0:
                col_0 = True
                break
        for y in range(n):
            if matrix[0][y] == 0:
                row_0 = True
                break

        for x in range(1, m):
            for y in range(1, n):
                if matrix[x][y] == 0:
                    matrix[x][0] = 0
                    matrix[0][y] = 0

        for x in range(1, m):
            for y in range(1, n):
                if matrix[x][0] == 0 or matrix[0][y] == 0:
                    matrix[x][y] = 0

        if col_0:
            for x in range(m):
                matrix[x][0] = 0

        if row_0:
            for y in range(n):
                matrix[0][y] = 0

        # Option 1 - Space O(m+n)
        """
        row = {}
        col = {}

        for x in range(m):
            for y in range(n):
                if matrix[x][y] == 0:
                    row[y] = col[x] = None

        for x in range(m):
            for y in range(n):
                if x in col or y in row:
                    matrix[x][y] = 0
        """
