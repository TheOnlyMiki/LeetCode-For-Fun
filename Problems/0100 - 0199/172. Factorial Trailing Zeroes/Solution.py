class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        output = 0
        while n/5:
            n /= 5
            output += n

        return output
