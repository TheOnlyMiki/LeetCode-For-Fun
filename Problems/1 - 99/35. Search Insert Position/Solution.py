class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Option 2 - Binary Search, Or call devide and conquer
        left, right = 0, len(nums)
        if nums[right-1] < target:
            return right

        mid = temp = None
        while left <= right:
            mid = (left + right) // 2
            temp = nums[mid]
            if target < temp:
                right = mid-1
            elif target > temp:
                left = mid+1
            else:
                return mid

        return left

        # Option 1 - Linear Method
        """
        for i, num in enumerate(nums):
            if num >= target:
                return i

        return len(nums)
        """
