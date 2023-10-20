class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        output = 0
        for num in sorted(nums)[::2]:
            output += num
        return output
