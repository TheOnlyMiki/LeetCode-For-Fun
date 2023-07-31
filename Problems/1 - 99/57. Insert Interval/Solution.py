class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        record = -1
        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[0]:
                break
            else:
                record = i

        intervals.insert(record + 1, newInterval)

        i = 0
        length = len(intervals)
        record_i = record_j = None
        output = []

        while i < length:
            record_i, record_j = intervals[i]

            while i + 1 < length and intervals[i+1][0] <= record_j:
                i += 1
                if record_j < intervals[i][1]:
                    record_j = intervals[i][1]

            output.append([record_i, record_j])
            i += 1

        return output

        # Not pass, part mistake.....
        """
        if len(intervals) == 0:
            return [newInterval]

        record = -1

        for i in range(len(intervals)):
            if intervals[i][0] <= newInterval[0]:
                record = i

        intervals.insert(record + 1, newInterval)

        if record == -1:
            record = 0

        i = record

        length = len(intervals)

        record_i, record_j = intervals[i]

        while i + 1 < length and intervals[i+1][0] <= record_j:
            i += 1
            if record_j < intervals[i][1]:
                record_j = intervals[i][1]

        newInterval = [record_i, record_j]
        print(intervals, record, i+1, newInterval)
        
        for index in range(record, i+1):
            del intervals[record] 

        print(intervals, record, i+1)

        intervals.insert(record, newInterval)
        
        return intervals
        """
