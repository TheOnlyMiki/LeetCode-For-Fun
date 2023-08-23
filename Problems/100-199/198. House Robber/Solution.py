class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #length = len(nums)
        record = {len(nums):0, len(nums)+1:0}

        def sumTheMoney(i):
            if i in record:
                return record[i]

            record[i] = max(nums[i] + sumTheMoney(i+2), sumTheMoney(i+1))
            return record[i]

        return sumTheMoney(0)
