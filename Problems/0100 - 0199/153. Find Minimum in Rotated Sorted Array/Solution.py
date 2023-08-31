class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left, right = 0, len(nums)-1
        
        if nums[left] < nums[right]:
            return nums[0]

        mid = None

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= nums[right]:
                left = mid+1
            else:
                right = mid

        return nums[right]
