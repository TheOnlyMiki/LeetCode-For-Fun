class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for num in nums:
            if 9 < num < 100 or 999 < num < 10000 or num == 100000:
                count += 1

        return count
