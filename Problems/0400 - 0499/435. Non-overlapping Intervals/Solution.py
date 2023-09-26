class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        output, end = 0, -1e5
        for i, j in sorted(intervals, key=lambda x:x[1]):
            if i < end:
                output += 1
            else:
                end = j

        return output
