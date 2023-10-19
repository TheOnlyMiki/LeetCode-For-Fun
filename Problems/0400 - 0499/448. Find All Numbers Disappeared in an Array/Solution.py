class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Option 2 - In palce, Time O(n), Space O(1)
        for num in nums:
            if nums[abs(num)-1] > 0:
                nums[abs(num)-1] *= -1

        return [i for i, num in enumerate(nums, start=1) if num > 0]

        # Option 1 - Hash Table, Time O(n), Space O(n)
        """
        return set(range(1, len(nums)+1)) - set(nums)
        """
