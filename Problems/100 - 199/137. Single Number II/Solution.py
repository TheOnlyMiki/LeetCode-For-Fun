class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Option 2 - Bit operation but some math
        output = 0
        consum = None
        for i in xrange(32):
            consum = 0
            for num in nums:
                if num < 0:
                    num = num & (2**32-1)
                consum += num >> i & 1
            if consum % 3 == 1:
                output += 2**i

        return output - 2**32 if output >= 2**31 else output

        # Option 1 - Time O(n) Space O(n)
        record1 = set()
        record2 = set()
        for num in nums:
            if num in record1:
                if num in record2:
                    record1.remove(num)
                else:
                    record2.add(num)
            else:
                record1.add(num)

        return record1.pop()
