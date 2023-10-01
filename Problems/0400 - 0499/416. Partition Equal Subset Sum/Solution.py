class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Option 2 - Dynamic Programming
        consum = sum(nums)
        if consum % 2 == 1:
            return False

        n = len(nums)
        consum = consum // 2
        totals = range(consum, -1, -1)

        record = [True] + [False] * consum
        for num in nums:
            for total in totals:
                if total >= num:
                    record[total] = record[total] or record[total-num]

        return record[consum]

        # Option 1 - Wrong, this is for single digit
        """
        maximum = 0
        consum = 0
        for num in nums:
            if num > maximum:
                maximum, num = num, maximum
            consum += num

        return maximum == consum
        """
