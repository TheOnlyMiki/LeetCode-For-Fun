class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x, current_duplicate_value = 1, nums[0]
        for i in range(1, len(nums)):
            current_value = nums[i]
            if current_value != current_duplicate_value:
                nums[x] = current_duplicate_value = current_value
                x+=1

        return x
