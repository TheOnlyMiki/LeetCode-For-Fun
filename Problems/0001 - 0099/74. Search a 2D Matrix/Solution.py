class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # Option 2 - Binary Search, or call devide and conquer
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m*n-1
        mid = temp = None

        while left <= right:
            mid = (left + right) // 2
            temp = matrix[mid//n][mid%n]
            if temp > target:
                right = mid - 1
            elif temp < target:
                left = mid + 1
            else:
                return True
        
        return False

        # Option 1 - Linear Method
        """
        end_pos = len(matrix[0]) - 1

        for i in xrange(len(matrix)):
            if target <= matrix[i][end_pos]:
                try:
                    matrix[i].index(target)
                    return True
                except:
                    return False

        return False
        """
