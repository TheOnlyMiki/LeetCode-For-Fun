class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Option 2
        return n > 0 and not (n & n - 1)

        # Option 1
        if n < 0:
            return False

        count = 0
        for i in range(32):
            if n & 1 == 1:
                count += 1

            n >>= 1

        return count == 1
