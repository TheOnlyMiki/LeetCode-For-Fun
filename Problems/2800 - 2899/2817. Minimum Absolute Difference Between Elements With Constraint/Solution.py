class Solution(object):
    def minAbsoluteDifference(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        def binarySearchIndex(num):
            right = len(self.sortedNums)
            if right == 0 or self.sortedNums[-1] <= num:
                return right

            left = 0
            mid = current = None
            while left <= right:
                mid = (left + right) // 2
                current = self.sortedNums[mid]
                if current < num:
                    left = mid+1
                elif current > num:
                    right = mid-1
                else:
                    return mid

            return left

        self.sortedNums = []
        self.length = 0
        output = 1e10

        num = index = None
        for i in range(x, len(nums)):
            num = nums[i-x]
            index = binarySearchIndex(num)
            if len(self.sortedNums) == index:
                self.sortedNums.append(num)
            else:
                self.sortedNums.insert(index, num)

            num = nums[i]
            index = binarySearchIndex(num)
            if index != 0:
                output = min(output, num - self.sortedNums[index-1])
            if index != len(self.sortedNums):
                output = min(output, self.sortedNums[index] - num)
            
        return output
