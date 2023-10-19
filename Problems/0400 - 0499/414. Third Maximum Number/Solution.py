class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Option 2 - Time O(n), Space O(n)
        """
        minimum = -(2**31+1)
        max_1, max_2, max_3 = minimum, minimum, minimum

        for num in set(nums):
            if num > max_1:
                max_1, max_2, max_3 = num, max_1, max_2
            elif num > max_2:
                max_2, max_3 = num, max_2
            elif num > max_3:
                max_3 = num

        '''
        for num in set(nums):
            if num > max_1:
                max_1, num = num, max_1
            if num > max_2:
                max_2, num = num, max_2
            if num > max_3:
                max_3 = num
        '''

        return max_3 if max_3 != minimum else max_1
        """

        # Option 1 - Time O(n), Space O(1)
        minimum = -(2**31+1)
        max_1, max_2, max_3 = minimum, minimum, minimum

        for num in nums:
            if num >= max_1:
                if num == max_1:
                    continue
                max_1, num = num, max_1
            if num >= max_2:
                if num == max_2:
                    continue
                max_2, num = num, max_2
            if num > max_3:
                max_3, num = num, max_3

        '''
        for num in nums:
            if num >= max_1:
                max_1, num = num, max_1 if num > max_1 else minimum
            if num >= max_2:
                max_2, num = num, max_2 if num > max_2 else minimum
            if num > max_3:
                max_3, num = num, max_3
        '''

        return max_3 if max_3 != minimum else max_1
