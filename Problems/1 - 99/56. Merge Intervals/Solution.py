class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        output = []

        intervals = sorted(intervals, key=lambda x:x[0])

        record_i, record_j = intervals[0] 

        for i in range(1, len(intervals)):
            if intervals[i][0] > record_j:
                output.append([record_i, record_j])
                record_i, record_j = intervals[i]
            else:
                if intervals[i][1] > record_j:
                    record_j = intervals[i][1]

        output.append([record_i, record_j])

        return output
        """

        # Option 1
        length = len(intervals)
        output = []
        i = 0 

        intervals = sorted(intervals, key=lambda x:x[0])

        record_i = record_j = None

        while i < length:
            record_i, record_j = intervals[i]

            while i + 1 < length and intervals[i+1][0] <= record_j:
                i += 1
                if record_j < intervals[i][1]:
                    record_j = intervals[i][1]

            output.append([record_i, record_j])
            i += 1

        return output
        """
