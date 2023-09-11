class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Option 2
        index = 0
        for i, num in enumerate(nums):
            if num == 0:
                k -= 1

            if k < 0:
                if nums[index] == 0:
                    k += 1
                index += 1

        return len(nums) - index

        # Option 1 - Cannot pass, over time
        """
        length = len(nums)
        i = output = 0
        temp = count = None

        if k == 0:
            while i < length:
                if nums[i] == 1:
                    temp, count = i, 0
                    while i < length and nums[i] == 1:
                        i += 1

                    if i - temp > output:
                        output = i - temp

                i += 1

            return output

        record = [None] * k

        while i < length:
            temp, count = i, 0
            while i < length and (count < k or nums[i] == 1):
                if nums[i] == 0:
                    record[count] = i
                    count += 1
                i += 1

            if i - temp > output:
                output = i - temp
            if i == length:
                break

            i = record[0] + 1

        return output
        """
