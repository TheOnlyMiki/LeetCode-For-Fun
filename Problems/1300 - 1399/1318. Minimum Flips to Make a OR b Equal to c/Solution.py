class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        count = 0
        for i in range(31, -1, -1):
            if c >> i & 1 == 1:
                if (a >> i & 1) | (b >> i & 1) == 0:
                    count += 1
            else:
                count += (a >> i & 1) + (b >> i & 1)
            
        return count
