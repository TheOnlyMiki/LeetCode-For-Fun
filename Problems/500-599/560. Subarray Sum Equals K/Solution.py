class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        sums = {}
        consum = 0
        output = 0

        for value in nums:
            if consum in sums:
                sums[consum] += 1
            else:
                sums[consum] = 1

            consum += value

            if consum - k in sums:
                output += sums[consum - k]
            
        return output
