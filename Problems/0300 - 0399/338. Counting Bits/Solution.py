class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        output = [0] * (n+1)
        temp1 = temp2 = None
        for i in range(1, n+1):
            temp1, temp2 = divmod(i, 2)
            output[i] = output[temp1] + temp2

        return output
