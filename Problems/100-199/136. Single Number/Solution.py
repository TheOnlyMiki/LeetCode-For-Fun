class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Option 2 - XOR: A^A^B = 0^B = B
        output = 0
        for num in nums:
            output ^= num

        return output

        # Option 1 - Time O(n) Space O(n)
        record = set()
        for num in nums:
            if num in record:
                record.remove(num)
            else:
                record.add(num)
        
        return record.pop()
