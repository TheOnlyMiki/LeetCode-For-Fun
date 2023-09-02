class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        index_0_insert, left, right = 0, 0, len(nums)-1

        while left <= right:
            if nums[left] == 0:
                nums[left], nums[index_0_insert] = nums[index_0_insert], nums[left]
                index_0_insert += 1
                left += 1
            elif nums[left] == 1:
                left += 1
            else:
                nums[right], nums[left] = nums[left], nums[right]
                right -= 1
