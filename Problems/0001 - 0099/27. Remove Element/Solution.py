class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # Option 2 - In place
        swap_i = 0
        for num in nums:
            if num != val:
                nums[swap_i] = num
                swap_i += 1

        return swap_i

        # Option 1 - extra spaces
        """
        nums_result = []
        val_nums = 0
        length_of_nums = len(nums)

        for i in range(length_of_nums):
            current_value = nums[i]
            if current_value != val:
                nums_result.append(current_value)
            else:
                val_nums+=1

        nums[:] = nums_result
        return length_of_nums - val_nums
        """
