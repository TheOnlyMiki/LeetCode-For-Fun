class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        i = 0
        num = None
        while i < length:
            num = nums[i]
            if 0 < num < length and nums[num-1] != num:
                nums[i], nums[num-1] = nums[num-1], num
            else:
                i += 1

        for i, num in enumerate(nums, start=1):
            if num != i:
                return i

        return length+1
