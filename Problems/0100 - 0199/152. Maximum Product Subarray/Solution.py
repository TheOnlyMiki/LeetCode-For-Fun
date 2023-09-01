class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        output = cur_min = cur_max = nums[0]

        for i in range(1, len(nums)):
            cur_min, cur_max = (nums[i] * cur_max, nums[i] * cur_min) if nums[i] < 0 else (nums[i] * cur_min, nums[i] * cur_max)
            if cur_max < nums[i]:
                cur_max = nums[i]
            if cur_min > nums[i]:
                cur_min = nums[i]
            if output < cur_max:
                output = cur_max

        return output
