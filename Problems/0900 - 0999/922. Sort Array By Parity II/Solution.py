class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length, left, right = len(nums), 0, 1
        while right < length:
            while left < length and nums[left] & 1 == 0:
                left += 2

            while right < length and nums[right] & 1 == 1:
                right += 2

            if right < length:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left+2, right+2

        return nums
