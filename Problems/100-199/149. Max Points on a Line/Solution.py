class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        length = len(points)
        if length < 3:
            return length

        output = 0
        x2 = y2 = None
        count = slope = None

        for i, (x1, y1) in enumerate(points):
            count = {}
            for index in xrange(i+1, length):
                x2, y2 = points[index]
                slope = None if x1 == x2 else float(y2 - y1) / (x2 - x1)
                count[slope] = count[slope]+1 if slope in count else 2
                output = max(count[slope], output)

        return output
