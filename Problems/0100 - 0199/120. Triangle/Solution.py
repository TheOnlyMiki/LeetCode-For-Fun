class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # Option 2 - Same time cost, space O(n) where n = len(triangle)
        next_level = None
        for i in xrange(len(triangle)-2, -1, -1):
            next_level = triangle[i+1]
            for j in xrange(len(triangle[i])):
                triangle[i][j] += min(next_level[j], next_level[j+1])

        return triangle[0][0]

        # Option 1 - Same time cost, but space O(whole triangle)
        """
        max_level = len(triangle)
        record = [ [100000]*len(n) for n in triangle ]

        def getSmallest(level, next1, next2):
            if level == max_level:
                return 0
            
            if record[level][next1] != 100000:
                record[level][next2] = getSmallest(level+1, next2, next2+1) + triangle[level][next2]
                return min(record[level][next1], record[level][next2])
            if record[level][next2] != 100000:
                record[level][next1] = getSmallest(level+1, next1, next2) + triangle[level][next1]
                return min(record[level][next1], record[level][next2])

            record[level][next1] = getSmallest(level+1, next1, next2) + triangle[level][next1]
            record[level][next2] = getSmallest(level+1, next2, next2+1) + triangle[level][next2]
            return min(record[level][next1], record[level][next2])
        
        return triangle[0][0] + getSmallest(1, 0, 1)
        """
