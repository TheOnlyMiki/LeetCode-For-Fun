class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # Option 2
        
        points = sorted(points, key =lambda x:x[1])
        record_j = points[0][1]
        output = 1

        for i in range(1, len(points)):
            if points[i][0] > record_j:
                output += 1
                record_j = points[i][1]

        return output
        

        # Option 1
        
        points = sorted(points, key =lambda x:x[0])

        i = 0
        length = len(points)
        record_j = None
        output = 0

        while i < length:
            record_j = points[i][1]

            while i+1 < length and points[i+1][0] <= record_j:
                i += 1
                if record_j > points[i][1]:
                    record_j = points[i][1]

            output += 1
            i += 1
        
        return output
