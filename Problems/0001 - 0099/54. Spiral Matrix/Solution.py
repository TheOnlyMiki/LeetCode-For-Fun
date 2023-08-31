class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        n = len(matrix[0])

        elements = m * n

        output = []
        
        left = 0
        right = n - 1
        top = 0
        bottom = m - 1

        direction = 0

        while len(output) != elements:
            direction = direction % 4
            # Handle left to right
            if direction == 0:
                output.extend(matrix[top][ left : right+1 ])
                top += 1
            # Handle top to bottom
            elif direction == 1:
                for i in range(top, bottom + 1):
                    output.append(matrix[i][right])
                right -= 1
            # Handle right to left
            elif direction == 2:
                temp = matrix[bottom][ left : right+1 ]
                output.extend(temp[::-1])
                bottom -= 1
            # Handle bottom to top
            else:
                for i in range(bottom, top - 1, -1):
                    output.append(matrix[i][left])
                left += 1
            
            direction += 1

        return output
