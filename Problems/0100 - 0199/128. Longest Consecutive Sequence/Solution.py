class Solution(object):
    # Option 2 - Same but less code and space O(n)
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        output = 0

        for num in nums:
            if num - 1 not in nums:
                max_num = num + 1
                while max_num in nums:
                    max_num += 1
                output = max(output, max_num - num)

        return output

    # Option 1 - Time O(n) and Space O(n + n)
    '''
    def countContinue(self, nums, check, direction):
        if check in nums:
            self.record.add(check)
            return self.countContinue(nums, check + direction, direction) + 1
        else:
            return 0

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.record = set()
        nums = set(nums)
        output = 0

        for num in nums:
            if num not in self.record:
                self.record.add(num)
                output = max(output, self.countContinue(nums, num-1, -1) + 1 + self.countContinue(nums, num+1, 1))

        return output
        '''
