class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        left, right = 1, max(piles)
        if len(piles) == h:
            return right

        def checkSpeed(speed):
            return sum((pile-1)//speed+1 for pile in piles) <= h

        temp = None
        while left < right:
            temp = (right + left) // 2
            if checkSpeed(temp):
                right = temp
            else:
                left = temp+1

        return left
