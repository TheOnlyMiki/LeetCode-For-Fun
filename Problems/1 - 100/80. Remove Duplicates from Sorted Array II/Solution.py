class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        x = 0
        duplicate = 0

        for value in nums:
            print(value, nums[x-1], duplicate)
            if value != nums[x-1]:
                duplicate = 1
                nums[x] = value
                x+=1
            elif duplicate < 2:
                duplicate+=1
                nums[x] = value
                x+=1

        return x
