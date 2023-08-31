class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = None
        if x < 0:
            s = -int( str(x)[::-1][:-1] )
        else:
            s = int( str(x)[::-1] )

        condition = 2**31
        if s >= 2**31 or s < -condition:
            return 0 

        return s
