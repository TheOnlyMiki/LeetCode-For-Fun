class Solution(object):
    def minimumReplacement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
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
