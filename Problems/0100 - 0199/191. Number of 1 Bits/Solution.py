class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        devide, remain = n, n
        count = 0
        while devide != 0:
            devide, remain = divmod(devide, 2)
            if remain == 1:
                count += 1

        return count
