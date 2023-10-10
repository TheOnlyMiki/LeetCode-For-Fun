class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Option 2 - Space O(1)
        k = k % len(nums)

        def swap(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left + 1, right - 1

        swap(0, len(nums)-1-k)
        swap(len(nums)-k, len(nums)-1)
        swap(0, len(nums)-1)
        
        # Option 1 - Space O(n)
        """
        shift_position = len(nums) - (k % len(nums))

        #return nums[shift_position:] + nums[:shift_position]

        nums[:] = nums[shift_position:] + nums[:shift_position]
        """
