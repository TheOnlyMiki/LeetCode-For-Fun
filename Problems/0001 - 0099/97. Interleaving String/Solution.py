class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        # Option 3 - Dynamic Program, Space O(m)
        if len(s1) + len(s2) != len(s3):
            return False

        length2 = len(s2) + 1
        record1 = [False] * length2
        record1[0] = True
        record2 = None
        s1_iteration = range(1, len(s1)+1)
        s2_iteration = range(1, length2)

        for i in s2_iteration:
            record1[i] = record1[i-1] and s2[i-1] == s3[i-1]

        for i in s1_iteration:
            record2 = [False] * length2
            record2[0] = record1[0] and s1[i-1] == s3[i-1]
            for j in s2_iteration:
                record2[j] = (
                    (record1[j] if s1[i-1] == s3[i+j-1] else False) or
                    (record2[j-1] if s2[j-1] == s3[i+j-1] else False)
                )
            
            record1 = record2
        
        return record1[-1]

        # Option 2 - Dynamic Program, Space O(m*n)
        """
        length1, length2 = len(s1), len(s2) + 1
        if length1 + length2 - 1 != len(s3):
            return False

        record = [ [False] * length2 for _ in s1 ]
        record.append([False] * length2)
        record[0][0] = True
        s1_iteration = range(1, length1+1)
        s2_iteration = range(1, length2)

        for i in s1_iteration:
            record[i][0] = record[i-1][0] and s1[i-1] == s3[i-1]

        for i in s2_iteration:
            record[0][i] = record[0][i-1] and s2[i-1] == s3[i-1]

        for i in s1_iteration:
            for j in s2_iteration:
                record[i][j] = (
                    (record[i-1][j] if s1[i-1] == s3[i+j-1] else False) or
                    (record[i][j-1] if s2[j-1] == s3[i+j-1] else False)
                )

        return record[-1][-1]
        """

        # Option 1 - Recursion, cannot pass, over time limit
        """
        length1, length2 = len(s1), len(s2)
        if length1 + length2 != len(s3):
            return False

        def DFS(x1, x2):
            if x1 == length1 and x2 == length2:
                return True

            return (
                (DFS(x1 + 1, x2) if x1 < length1 and s1[x1] == s3[x1+x2] else False) or 
                (DFS(x1, x2 + 1) if x2 < length2 and s2[x2] == s3[x1+x2] else False)
            )

        return DFS(0, 0)
        """
