class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # Option 2 - Dynamic Program, Space O(n)
        length2 = len(matrix[0])+1
        cols = range(1, length2)

        record1 = [0]*length2
        record2 = None

        output = 0
        previou_i = None
        for i in range(1, len(matrix)+1):
            record2 = [0]*length2
            previou_i = i-1
            for j in cols:
                if matrix[previou_i][j-1] == '1':
                    record2[j] = min(record1[j], record2[j-1], record1[j-1]) + 1
                if output < record2[j]:
                    output = record2[j]

            record1 = record2
        
        return output**2

        # Option 1 - Dynamic Program, Space O(m*n)
        """
        length2 = len(matrix[0])+1
        cols = range(1, length2)

        record = [[0]*length2 for _ in matrix]
        record.append([0]*length2)

        output = 0

        previou_i = None
        for i in range(1, len(record)):
            previou_i = i-1
            for j in cols:
                if matrix[previou_i][j-1] == '1':
                    record[i][j] = min(record[previou_i][j], record[i][j-1], record[previou_i][j-1]) + 1
                if output < record[i][j]:
                    output = record[i][j]
        
        return output**2
        """
