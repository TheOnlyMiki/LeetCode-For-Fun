class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Option 2 - Less code, but cost O(n) + O(nlogn) + O(n) -> nums[:] + sorted + set()
        nums[:] = sorted(set(nums))
        return len(nums)

        # Option 1 - This usually less operations than Option 1
        """
        x, current_duplicate_value = 1, nums[0]
        for i in range(1, len(nums)):
            if nums[i] != current_duplicate_value:
                nums[x] = current_duplicate_value = nums[i]
                x+=1

        return x
        """
