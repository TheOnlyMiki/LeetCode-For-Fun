class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # Option 2 - Dynamic Program, Space O(n)
        length2 = len(word2)+1
        record1 = range(length2)
        record2 = None

        word2_iteration = range(1, length2)

        for i in range(1, len(word1)+1):
            record2 = range(length2)
            record2[0] = record1[0] + 1
            for j in word2_iteration:
                record2[j] = record1[j-1] if word1[i-1] == word2[j-1] else min(record1[j-1], record1[j], record2[j-1]) + 1

            record1 = record2

        return record1[-1]

        # Option 1 - Dynamic Program, Space O(m*n)
        """
        length2 = len(word2)+1
        record = [ range(length2) for _ in word1]
        record.append(range(length2))
        word1_iteration = range(1, len(record))
        word2_iteration = range(1, length2)

        for i in word1_iteration:
            record[i][0] = record[i-1][0] + 1

        previou_i = None
        for i in word1_iteration:
            previou_i = i-1
            for j in word2_iteration:
                record[i][j] = record[previou_i][j-1] if word1[i-1] == word2[j-1] else min(record[previou_i][j-1], record[previou_i][j], record[i][j-1]) + 1
            
        return record[-1][-1]
        """
