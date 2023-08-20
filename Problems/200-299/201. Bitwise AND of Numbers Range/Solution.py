class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        output = 0
        temp = left ^ right
        for i in xrange(31, -1, -1):
            if temp >> i & 1 == 1:
                break
            elif left >> i & 1 == 1:
                output += 2**i

        return output
