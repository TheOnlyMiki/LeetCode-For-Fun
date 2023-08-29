class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        count = [0]*(amount + 1)
        count[0] = 1

        for coin in coins:
            for i in range(coin, amount+1):
                count[i] += count[i-coin]

        return count[amount]
