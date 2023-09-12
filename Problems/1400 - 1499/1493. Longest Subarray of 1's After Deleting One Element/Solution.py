class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index, k = 0, 1
        for i, num in enumerate(nums):
            if num == 0:
                k -= 1

            if k < 0:
                if nums[index] == 0:
                    k += 1
                index += 1

        return len(nums) - index - 1
