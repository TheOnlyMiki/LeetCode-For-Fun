class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        output = []
        n = len(nums)
        left = [1]*n
        right = [1]*n

        #Left
        initial = 1
        for i in range(1, n):
            left[i] = initial * nums[i-1]
            initial = left[i]

        #Right
        initial = 1
        for i in range(1, n):
            right[i] = initial * nums[-i]
            initial = right[i]

        #Combination
        for i in range(n):
            output.append(left[i] * right[-i-1])

        return output
