class Solution(object):
    def minimizeMax(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        nums = sorted(nums)
        length = len(nums)
        left, right = 0, nums[-1] - nums[0]
        mid = i = count = None

        while left < right:
            mid = (left + right) / 2
            i = 1
            count = 0

            while i < length:
                if nums[i] - nums[i-1] <= mid:
                    count += 1
                    i += 1
                i += 1

            if count < p:
                left = mid+1
            else:
                right = mid

        return left
