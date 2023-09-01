class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        consum = len(nums) * (len(nums)+1) // 2
        return consum - sum(nums)
