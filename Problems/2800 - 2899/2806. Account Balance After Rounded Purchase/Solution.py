class Solution(object):
    def accountBalanceAfterPurchase(self, purchaseAmount):
        """
        :type purchaseAmount: int
        :rtype: int
        """
        n = purchaseAmount / 5
        return 100 - n*5 if n % 2 == 0 else 100 - (n+1)*5
