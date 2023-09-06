class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums)-1

        break_point = -1
        for i in range(length, 0, -1):
            if nums[i] > nums[i-1]:
                break_point = i-1
                break

        if break_point != -1:
            swap = nums[break_point]
            for i in range(len(nums)-1, break_point, -1):
                if nums[i] > swap:
                    nums[break_point], nums[i] = nums[i], swap
                    break

        left, right = break_point+1, length
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
