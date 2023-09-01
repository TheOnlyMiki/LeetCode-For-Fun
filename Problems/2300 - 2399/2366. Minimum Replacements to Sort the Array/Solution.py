class Solution(object):
    def minimumReplacement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Option 2
        output = 0
        previou_lower = nums[-1]
        temp = None

        for i in range(len(nums)-2, -1, -1):
        #for num in nums[::-1]:
            if previou_lower < nums[i]:
                temp = (previou_lower + nums[i] - 1) / previou_lower
                nums[i] /= temp
                output += temp - 1
            
            previou_lower = nums[i]

        return output
        
        # Option 1
        output = 0
        previou_lower = nums[-1]
        temp1 = temp2 = None

        for i in range(len(nums)-2, -1, -1):
            if previou_lower < nums[i]:
                temp1, temp2 = divmod(nums[i], previou_lower)
                if temp2 > 0:
                    temp1 += 1

                nums[i] //= temp1
                output += temp1 - 1

            previou_lower = nums[i]

        return output
