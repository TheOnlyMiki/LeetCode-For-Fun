# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        while left <= n:
            mid = (left + n) // 2
            temp = guess(mid)
            if temp == -1:
                n = mid - 1
            elif temp == 1:
                left = mid + 1
            else:
                return mid

        return -1
