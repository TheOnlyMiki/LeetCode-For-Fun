class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Option 2 - Slow and fast pointers
        length = len(nums)
        left, right = 0, 1

        while right < length:
            while left < right and nums[left] != 0:
                left += 1

            while right < length and nums[right] == 0:
                right += 1

            if right == length:
                break

            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right += 1

        # Option 1 - Cannot pass, cause answer requires sorted?
        """
        left, right = 0, len(nums)-1

        while left < right:
            while left < right and nums[left] != 0:
                left += 1

            while left < right and nums[right] == 0:
                right -= 1

            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        """
