class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        point = 0
        record = len(nums) + 1
        consum = 0

        for i, num in enumerate(nums):
            consum += num
            while consum >= target:
                consum -= nums[point]
                record = min(record, i-point+1)
                point+=1

        if record > len(nums):
            return 0

        return record
