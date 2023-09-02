class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        record1 = [1] * n
        cols = range(1, n)

        for i in range(m-1):
            record2 = [1] * n
            for j in cols:
                record2[j] = record1[j] + record2[j-1]
            
            record1 = record2

        return record1[-1]
