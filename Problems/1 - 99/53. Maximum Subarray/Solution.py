class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        consum = 0
        record = -100000

        for num in nums:
            consum += num
            if consum > record:
                record = consum
            if consum < 0:
                consum = 0

            # Option 1
            """
            consum += num
            consum = max(num, consum)
            if consum > record:
                record = consum
            """

        return record
