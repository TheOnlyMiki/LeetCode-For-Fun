class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows = len(matrix)
        left, right = 0, len(matrix[0])-1
        while left != rows and right != -1:
            if target > matrix[left][right]:
                left += 1
            elif target < matrix[left][right]:
                right -= 1
            else:
                return True

        return False
