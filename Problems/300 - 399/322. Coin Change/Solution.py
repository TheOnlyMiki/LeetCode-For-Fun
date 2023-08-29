class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0

        limit = amount + 1
        record = [limit] * limit
        for coin in coins:
            if coin < limit:
                record[coin] = 1

        temp = None

        for num in xrange(limit):
            if record[num] != limit:
                for coin in coins:
                    temp = num + coin
                    if temp < limit:
                        record[temp] = min(record[num] + 1, record[temp])

        return -1 if record[-1] == limit else record[-1]
