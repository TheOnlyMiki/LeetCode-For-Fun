class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Option 2 - Binary Search, or call devide and conquer
        length = len(nums) - 1
        if length == 0:
            return 0
            
        left, right = 0, length
        mid = temp = None

        while left <= right:
            mid = (left + right) // 2
            temp = nums[mid]
            if (mid == 0 or temp > nums[mid-1]) and (mid == length or temp > nums[mid+1]):
                return mid
            
            if temp < nums[mid+1]:
                left = mid + 1
            else:
                right = mid - 1

        return 0

        # Option 1 - Linear Method
        """
        length = len(nums)
        if length == 1:
            return 0

        neighbor = None
        for i, num in enumerate(nums):
            if i-1 == -1:
                neighbor = max(num-1, nums[i+1])
            elif i+1 == length:
                neighbor = max(nums[i-1], num-1)
            else:
                neighbor = max(nums[i-1], nums[i+1])
            
            if neighbor < num:
                return i

        return 0
        """
