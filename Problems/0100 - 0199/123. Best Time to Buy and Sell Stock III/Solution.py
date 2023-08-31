class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Option 3
        pre_low1 = pre_low2 = 200000
        profit1 = profit2 = 0
        for price in prices:
            if pre_low1 > price:
                pre_low1 = price

            if profit1 < price - pre_low1:
                profit1 = price - pre_low1

            if pre_low2 > price - profit1:
                pre_low2 = price - profit1

            if profit2 < price - pre_low2:
                profit2 = price - pre_low2

        return profit2

        # Option 2 - Incorrect
        """
        record = [[0, 0]] * (len(prices)+1)
        pre_low = prices[0]

        for i, price in enumerate(prices, start=1):
            if pre_low > price:
                pre_low = price

            current_profit = price - pre_low
            
            record[i] = [current_profit, i] if record[i-1][0] < current_profit else record[i-1]

        output = record[-1][0]
        for i, price in enumerate(prices, start=1):
            if prices[record[i-1][1]] > price:
                record[i][1] = i-1
                continue
            
            current_profit = record[i-1][0] + price - prices[record[i-1][1]]
            
            if current_profit > output:
                output = current_profit

        return output
        """

        # Option 1 - Cannot pass
        """
        total_profit = 0
        profit = 0
        pre_low = prices[0]
        for i, price in enumerate(prices):
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
