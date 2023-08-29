class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        col_len = len(matrix)
        row_len = len(matrix[0])
        m = col_len - 1
        n = row_len - 1

        for x in range(col_len//2):
            for y in range(row_len):
                temp = matrix[x][y]
                matrix[x][y] = matrix[m-x][y]
                matrix[m-x][y] = temp
        
        for x in range(col_len):
            for y in range(x, row_len):
                temp = matrix[x][y]
                matrix[x][y] = matrix[y][x]
                matrix[y][x] = temp

        #print(matrix)

        # Not in place method
        # Rotae 90
        """
        m = len(matrix) - 1
        n = len(matrix[0]) - 1

        temp_matrix = [ row[:] for row in matrix ]

        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                matrix[x][y] = temp_matrix[m-y][x]

        #print(matrix)
        """

        # Rotate 180
        """
        m = len(matrix) - 1
        n = len(matrix[0]) - 1

        temp_matrix = [ row[:] for row in matrix ]

        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                matrix[x][y] = temp_matrix[m-x][n-y]

        #print(matrix)
        """

        # Rotate -90
        """
        m = len(matrix) - 1
        n = len(matrix[0]) - 1

        temp_matrix = [ row[:] for row in matrix ]

        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                matrix[x][y] = temp_matrix[y][n-x]

        #print(matrix)
        """
