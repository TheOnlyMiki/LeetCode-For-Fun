class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 0
        right = x
        mid = None
        temp = None
        while left <= right:
            mid = (left + right) / 2
            temp = mid*mid
            if temp < x:
                left = mid+1
            elif temp > x:
                right = mid-1
            else:
                return mid

        return left-1
