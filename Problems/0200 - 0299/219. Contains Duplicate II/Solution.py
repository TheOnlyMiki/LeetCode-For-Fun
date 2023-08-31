class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        count = {}
        for i, num in enumerate(nums):
            if num in count and i - count[num] <= k:
                    return True
            count[num] = i

        return False
