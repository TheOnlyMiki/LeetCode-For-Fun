class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Option 2
        x = 0
        duplicate = 0

        for value in nums:
            if duplicate < 2 or value != nums[x-1]:
                if value != nums[x-1]:
                    duplicate = 0
                duplicate+=1
                nums[x] = value
                x+=1

        return x
        
        # Option 1
        """
        x = 1
        duplicate_value = nums[0]
        duplicate_allow = True

        for i in range(1, len(nums)):
            if duplicate_value != nums[i]:
                nums[x] = duplicate_value = nums[i]
                duplicate_allow = True
                x+=1
            elif duplicate_allow:
                nums[x] = duplicate_value
                duplicate_allow = False
                x+=1

        return x
        """
