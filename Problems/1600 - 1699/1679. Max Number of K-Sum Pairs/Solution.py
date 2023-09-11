class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        output = 0
        record = {}
        temp = None
        for num in nums:
            temp = k - num
            if temp in record and record[temp] > 0:
                output += 1
                record[temp] -= 1
            else:
                if num in record:
                    record[num] += 1
                else:
                    record[num] = 1

        return output
