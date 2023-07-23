class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        profit = 0
        pre_low = prices[0]
        for price in prices:
            if pre_low < price:
                profit += price - pre_low
            pre_low = price

        return profit

        """
        #First, I thought the question says you can only hold 1 stock and only can trade 
        #up to two times, and only if you sold the stock you have been held, then you can 
        #purchased the new stock :(

        total_profit = 0
        profit = 0
        pre_low = prices[0]
        for i in range(len(prices)):
            price = prices[i]

            if pre_low > price:
                pre_low = price
                continue

            current_profit = price - pre_low
            
            if profit < current_profit:
                profit = current_profit

                #Calculate the remainer maximum profit
                profit_2 = 0
                pre_low_2 = price
                for price_2 in prices[i+1:]:
                    if pre_low_2 > price_2:
                        pre_low_2 = price_2
                        continue

                    current_profit_2 = price_2 - pre_low_2
                    
                    if profit_2 < current_profit_2:
                        profit_2 = current_profit_2
                
                current_total_profit = profit + profit_2
                if total_profit < current_total_profit:
                    total_profit = current_total_profit

        return total_profit
        """
