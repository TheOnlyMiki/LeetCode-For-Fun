class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = [1]
        n = len(nums)

        #Option 2
        for i in range(1, n):
            output.append(output[i-1] * nums[i-1])

        record = 1
        for i in range(n-1, -1, -1):
            output[i] = record * output[i]
            record = record * nums[i]

        return output

        #Option 1
        """
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
        """
