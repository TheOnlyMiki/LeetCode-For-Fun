class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        devide = (n, n)
        count = 0
        while devide[0] != 0:
            devide = divmod(devide[0], 2)
            if devide[1] == 1:
                count += 1

        return count
