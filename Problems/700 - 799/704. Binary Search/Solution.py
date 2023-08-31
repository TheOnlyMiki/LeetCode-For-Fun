class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums)-1
        mid = current = None

        while left <= right:
            mid = (left + right) // 2
            current = nums[mid]
            if current > target:
                right = mid - 1
            elif current < target:
                left = mid + 1
            else:
                return mid

        return -1
