class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        pre_low = [2000]*k
        profit = [0]*k
        iteration = range(1, k)

        for price in prices:
            if pre_low[0] > price:
                pre_low[0] = price

            if profit[0] < price - pre_low[0]:
                profit[0] = price - pre_low[0]

            for i in iteration:
                if pre_low[i] > price - profit[i-1]:
                    pre_low[i] = price - profit[i-1]

                if profit[i] < price - pre_low[i]:
                    profit[i] = price - pre_low[i]

        return profit[-1]
