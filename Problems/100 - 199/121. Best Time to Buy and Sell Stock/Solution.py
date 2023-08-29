class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        pre_low = prices[0]
        for price in prices:
            if pre_low > price:
                pre_low = price
                continue

            #profit = max(profit, price - pre_low)
            
            if profit < price - pre_low:
                profit = price - pre_low
            

        return profit
