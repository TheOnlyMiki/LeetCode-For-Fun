class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        remain = {}
        for i, num in enumerate(nums):
            if target - num in remain:
                remain = [remain[target - num], i]
                break
            remain[num] = i

        return remain
