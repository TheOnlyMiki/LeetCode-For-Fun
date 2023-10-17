class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        output, count = 0, 0
        for num in nums:
            if num == 0:
                count = 0
            else:
                count += 1
                if count > output:
                    output = count

        return output
