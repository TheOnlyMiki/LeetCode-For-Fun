class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        #n = len(nums)
        #k_new = k % n
        shift_position = len(nums) - (k % len(nums))

        #return nums[shift_position:] + nums[:shift_position]

        nums[:] = nums[shift_position:] + nums[:shift_position]
