class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        buy = -1e7
        output = 0
        for num in prices:
            temp = output

            if output < buy + num:
                output = buy + num

            if buy < temp - num - fee:
                buy = temp - num - fee

        return output
