class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # Option 2 - XOR
        xor, count = x^y, 0
        while xor != 0:
            if xor & 1 == 1:
                count += 1
            xor >>= 1
            
        return count

        # Option 1 - Count of different bits
        """
        count = 0
        while x != y:
            if x & 1 != y & 1:
                count += 1

            x, y = x >> 1, y >> 1
        
        return count
        """
