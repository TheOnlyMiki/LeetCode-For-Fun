class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        # Option 2
        output = []
        nums_len = len(nums)
        i = 0

        while i < nums_len:
            num = nums[i]

            while i + 1 < nums_len and nums[i] + 1 == nums[i+1]:
                i += 1

            if nums[i] == num:
                output.append(str(num))
            else:
                output.append(str(num)+"->"+str(nums[i]))

            i += 1

        return output

        # Option 1
        """
        if len(nums) == 0:
            return []

        output = []
        start = nums[0]
        end = start

        for num in nums[1:]:
            if num != end + 1:
                if start == end:
                    output.append(str(start))
                else:
                    output.append(str(start)+"->"+str(end))
                start = end = num

            end = num

        # Handle the remain
        if start == end:
            output.append(str(start))
        else:
            output.append(str(start)+"->"+str(end))

        return output
        """
