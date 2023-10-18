class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        increase = True
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                if increase and nums[0] >= nums[i]:
                    increase = False
                else:
                    return False

        return increase or nums[-1] <= nums[0]
