class Solution(object):
    def numTilings(self, n):
        """
        :type n: int
        :rtype: int
        """
        mod = 1e9+7
        previou = [1, 2, 5]
        if n < 4:
            return previou[n-1]

        for _ in range(n-3):
            previou[:] = previou[1], previou[2], (previou[2] * 2 + previou[0]) % mod

        return int(previou[2])
