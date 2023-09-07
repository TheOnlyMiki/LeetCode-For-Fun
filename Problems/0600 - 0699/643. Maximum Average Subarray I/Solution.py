class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        output = consum = sum(nums[i] for i in range(k))

        for i in range(len(nums)-k):
            consum += nums[i+k] - nums[i]

            if consum > output:
                output = consum
        
        return output / float(k)
