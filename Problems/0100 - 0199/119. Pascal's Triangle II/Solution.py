class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row, current = 0, [1]
        while rowIndex != row:
            next_level = [1]
            for i in range(1, len(current)):
                next_level.append(current[i] + current[i-1])
            
            current = next_level + [1]
            row += 1

        return current
