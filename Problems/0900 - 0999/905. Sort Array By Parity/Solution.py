class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left, right = 0, len(nums)-1
        while left < right:
            while left < right and nums[left] & 1 == 0:
                left += 1

            while left < right and nums[right] & 1 == 1:
                right -= 1

            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left+1, right-1

        return nums
