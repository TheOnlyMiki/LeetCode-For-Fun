class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
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
