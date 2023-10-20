class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index, max_1, max_2 = -1, -1, -1
        for i, num in enumerate(nums):
            if num > max_1:
                index, max_1, max_2 = i, num, max_1
            elif num > max_2:
                max_2 = num

        return -1 if max_1 < max_2 * 2 else index
