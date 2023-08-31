class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        record = {}
        for num in nums:
            if num in record:
                record[num] += 1
            else:
                record[num] = 1

        record = sorted(record.items(), key=(lambda x:x[1]))

        output = []
        for _ in range(k):
            output.append(record.pop()[0])

        return output
