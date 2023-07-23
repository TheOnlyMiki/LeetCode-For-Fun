class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        last_index = len(nums) - 1
        if sum(nums[1:-1]) > last_index:
            return True

        return False
