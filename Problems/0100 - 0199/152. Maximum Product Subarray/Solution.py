class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        output = num = cur_min = cur_max = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            
            cur_min, cur_max = (num * cur_max, num * cur_min) if num < 0 else (num * cur_min, num * cur_max)
            if cur_max < num:
                cur_max = num
            if cur_min > num:
                cur_min = num
            if output < cur_max:
                output = cur_max

        return output
