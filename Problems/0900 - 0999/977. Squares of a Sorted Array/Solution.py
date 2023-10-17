class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Option 3 - Two pointer, but only traversal once N, Time O(n)
        output = [0] * len(nums)
        left, right, i = 0, len(nums)-1, len(nums)-1
        while i != -1:
            if abs(nums[right]) > abs(nums[left]):
                output[i] = nums[right]**2
                right, i = right-1, i-1
            else:
                output[i] = nums[left]**2
                left, i = left+1, i-1

        return output

        # Option 2 - Two pointer, but needs traversal twice N, Time O(n)
        """
        length = len(nums)
        negative = positive = None
        negatives, positives = [], []

        for i in range(length):
            if nums[i] >= 0:
                negative, positive = i-1, i
                break
            negatives.append(nums[i]**2)

        if positive == None:
            return negatives[::-1]

        positives = [nums[i]**2 for i in range(positive, length)]
        
        length, positive, i = len(positives), 0, 0
        for i in range(len(nums)):
            if negative == -1:
                nums[i], positive = positives[positive], positive+1
            elif positive == length:
                nums[i], negative = negatives[negative], negative-1
            elif negatives[negative] < positives[positive]:
                nums[i], negative = negatives[negative], negative-1
            else:
                nums[i], positive = positives[positive], positive+1

        return nums
        """

        # Option 1
        """
        for i, num in enumerate(nums):
            nums[i] *= num

        nums.sort()
        return nums
        """
